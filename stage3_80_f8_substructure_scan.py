#!/usr/bin/env python3
"""Stage 3.80/F8a: cold co-moving substructure phase-space screen.

Branches
--------
mini
    Pre-solar virialised Plummer mini-halo. sigma is derived from M_sub and
    r_core. The F7 adiabatic upper-bound phase-space mapping is used. A reduced
    birth-cluster survival proxy is retained as a screening diagnostic.

stream
    Pre-solar unbound Gaussian clump / finite stream segment. sigma and v_rel
    are independent. Ballistic expansion and bulk drift during proto-solar
    collapse are included before the same F7 phase-space mapping.

torus
    Post-collapse / embryo-epoch co-moving torus target state at 1 AU. This
    branch does NOT reapply the F7 mapping. It integrates the actual torus mass
    intersecting the 0.03-M_E proto-Earth Hill sphere and imposes an epicyclic
    width gate w >= sigma/Omega. This closes two loopholes in the first draft:
    local rho*V_H cannot be used for streams narrower than r_H, and width and
    random velocity cannot be chosen independently for an unconfined Keplerian
    torus.

The module is a reduced screening model, not a formation proof.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.stats import ncx2

G = 6.67430e-11
M_SUN = 1.98847e30
M_EARTH = 5.97219e24
AU = 1.495978707e11
PC = 3.085677581e16
MYR = 1e6 * 365.25 * 86400

F6_M1 = 0.03 * M_EARTH
F6_MU_REQ = 8.318
F6_RH = AU * (F6_M1 / (3 * M_SUN)) ** (1 / 3)
F6_VH = 4 * math.pi * F6_RH**3 / 3
SEED_MASSES = (1e10, 1e11, 2e11, 5e11)
BENNU_RHO = 3.3e-15
CLUSTERS = {"low": (1e2, 1.4), "med": (1e3, 2.0), "high": (1e4, 2.9)}
DEFAULT_V_ELIGIBLE_KMS = 1.0


def plummer_density(r, M, a):
    return 3 * M / (4 * math.pi * a**3) * (1 + (r / a) ** 2) ** -2.5


def plummer_sigma_1d(r, M, a):
    return math.sqrt(G * M / (6 * a) / math.sqrt(1 + (r / a) ** 2))


def plummer_mass_enclosed(r, M, a):
    return M * r**3 / (r * r + a * a) ** 1.5


def gaussian_density(r, M, a):
    return M / ((2 * math.pi) ** 1.5 * a**3) * math.exp(-0.5 * (r / a) ** 2)


def mapping_factor(r=AU):
    return 4 / (3 * math.sqrt(math.pi)) * (G * M_SUN / r) ** 1.5


def rho_required(seed_mass, mu=F6_MU_REQ):
    return mu * seed_mass / F6_VH


def q_required(seed_mass, mu=F6_MU_REQ):
    return rho_required(seed_mass, mu) / mapping_factor()


def q_to_msun_pc3_kms3(q):
    return q * (PC**3 / M_SUN) * 1e9


def mu_from_density(rho, seed_mass):
    return rho / seed_mass * F6_VH


def shifted_q(rho, sigma, vrel):
    if rho <= 0 or sigma <= 0:
        return 0.0
    x = -0.5 * (vrel / sigma) ** 2
    return 0.0 if x < -745 else rho / sigma**3 * math.exp(x)


def vrel_grid(n):
    a = np.array([0, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 0.6, 1.0])
    if n <= len(a):
        return np.unique(a[np.linspace(0, len(a) - 1, n).round().astype(int)])
    return np.unique(np.r_[0, np.geomspace(1e-4, 1, n - 1)])


def cluster_survival(M, a, model="med", t_myr=10):
    """Reduced smooth-tide + single-impulse stellar-encounter stress proxy."""
    n_pc3, v_kms = CLUSTERS[model]
    v = v_kms * 1e3
    ms = 0.5 * M_SUN
    rh = 1.30476603 * a
    rhoh = 0.5 * M / (4 * math.pi * rh**3 / 3)
    rhocl = n_pc3 * ms / PC**3
    tide = rhoh > 3 * rhocl
    ebind = 3 * math.pi * G * M / (64 * a)
    b = ((4 / 3) * G**2 * ms**2 * rh**2 / (v * v * ebind)) ** 0.25
    foc = 1 + 2 * G * (M + ms) / (b * v * v)
    rate = n_pc3 / PC**3 * math.pi * b * b * foc * v
    return (math.exp(-rate * t_myr * MYR) if tide else 0.0), b / AU, tide


def torus_peak_density(M, R, w):
    return M / (4 * math.pi**2 * R * w**2)


@lru_cache(maxsize=16384)
def velocity_eligible_fraction(sigma_ms, vrel_ms, vmax_ms):
    if sigma_ms <= 0 or vrel_ms < 0 or vmax_ms < 0:
        raise ValueError("invalid velocity arguments")
    return float(ncx2.cdf((vmax_ms / sigma_ms) ** 2, df=3, nc=(vrel_ms / sigma_ms) ** 2))


@lru_cache(maxsize=4096)
def _torus_hill_fraction_cached(q, eps):
    if q <= 0 or eps <= 0:
        raise ValueError("invalid torus ratios")
    integrand = lambda u: u * math.sqrt(max(0.0, 1 - u * u)) * math.exp(-0.5 * (u / q) ** 2)
    I, _ = quad(integrand, 0.0, 1.0, epsabs=1e-12, epsrel=1e-10, limit=200)
    frac = eps * I / (math.pi * q * q)
    return min(1.0, max(0.0, frac))


def torus_hill_spatial_fraction(width_m):
    return _torus_hill_fraction_cached(round(width_m / F6_RH, 12), round(F6_RH / AU, 12))


def solar_omega_1au():
    return math.sqrt(G * M_SUN / AU**3)


def torus_requirement(sigma_kms, vrel_kms=0.0, v_eligible_kms=DEFAULT_V_ELIGIBLE_KMS):
    sigma = sigma_kms * 1e3
    w = sigma / solar_omega_1au()
    fsp = torus_hill_spatial_fraction(w)
    fvel = velocity_eligible_fraction(sigma, vrel_kms * 1e3, v_eligible_kms * 1e3)
    nreq = math.inf if fsp <= 0 or fvel <= 0 else F6_MU_REQ / (fsp * fvel)
    return dict(width_AU=w / AU, hill_spatial_fraction=fsp, velocity_fraction=fvel, Nseed_required=nreq)


@dataclass
class Grid:
    branch: str = "both"
    mmin: float = 1e-15
    mmax: float = 1e-4
    mn: int = 10
    rmin: float = 1e-3
    rmax: float = 1e3
    rn: int = 12
    smin: float = 0.01
    smax: float = 1.0
    sn: int = 8
    vn: int = 6
    collapse_myr: float = 0.06
    cluster: str = "med"


@dataclass
class TorusGrid:
    mmin: float = 1e-18
    mmax: float = 1e-6
    mn: int = 40
    wmin: float = 1e-4
    wmax: float = 0.3
    wn: int = 24
    smin: float = 0.01
    smax: float = 2.0
    sn: int = 30
    vn: int = 5
    v_eligible_kms: float = DEFAULT_V_ELIGIBLE_KMS


def _row(branch, Mms, rau, sig_kms, v_kms, seed, rho, sig, q):
    mapped = mapping_factor() * q
    mu = mu_from_density(mapped, seed)
    return dict(branch=branch,Msub_Msun=Mms,rcore_AU=rau,sigma_input_kms=sig_kms,
        vrel_kms=v_kms,seedmass_kg=seed,rho_phase_kgm3=rho,sigma_phase_ms=sig,
        Qeff=q,Qeff_Msun_pc3_per_kms3=q_to_msun_pc3_kms3(q),
        rho_mapped_1AU_kgm3=mapped,mu_H_mapped=mu,
        f_seed_required=(math.inf if mu<=0 else F6_MU_REQ/mu),phase_space_pass=mu>=F6_MU_REQ)


def scan_mini(g: Grid):
    rows=[]; t=g.collapse_myr*MYR
    for Mms in np.logspace(np.log10(g.mmin),np.log10(g.mmax),g.mn):
      M=Mms*M_SUN
      for rau in np.logspace(np.log10(g.rmin),np.log10(g.rmax),g.rn):
        a=rau*AU; p,b,tide=cluster_survival(M,a,g.cluster)
        rho1=plummer_density(AU,M,a); menc=plummer_mass_enclosed(AU,M,a)/M_SUN
        for vk in vrel_grid(g.vn):
          d=vk*1e3*t; rho=plummer_density(d,M,a); sig=plummer_sigma_1d(d,M,a)
          q=shifted_q(rho,sig,vk*1e3)
          for seed in SEED_MASSES:
            r=_row('mini',Mms,rau,np.nan,vk,seed,rho,sig,q)
            r.update(cluster_survival_prob=p,b_disrupt_AU=b,smooth_tide_pass=tide,
                overlap_offset_AU=d/AU,rho_profile_1AU_kgm3=rho1,Menc_1AU_Msun=menc)
            retained=max(rho1,r['rho_mapped_1AU_kgm3'])
            r['rho_if_retained_today_kgm3']=retained
            r['present_day_if_retained_pass']=retained<=BENNU_RHO
            r['stage1_candidate']=r['phase_space_pass'] and r['f_seed_required']<=1 and p>0.1
            r['stage1_candidate_if_retained_today']=r['stage1_candidate'] and r['present_day_if_retained_pass']
            rows.append(r)
    return pd.DataFrame(rows)


def scan_stream(g: Grid):
    rows=[]; t=g.collapse_myr*MYR
    for Mms in np.logspace(np.log10(g.mmin),np.log10(g.mmax),g.mn):
      M=Mms*M_SUN
      for rau in np.logspace(np.log10(g.rmin),np.log10(g.rmax),g.rn):
        a0=rau*AU; rho0=gaussian_density(0,M,a0); rho1=gaussian_density(AU,M,a0)
        for sk in np.geomspace(g.smin,g.smax,g.sn):
          sig=sk*1e3
          for vk in vrel_grid(g.vn):
            at=math.sqrt(a0*a0+(sig*t)**2); off=vk*1e3*t
            rho=gaussian_density(off,M,at); q=shifted_q(rho,sig,vk*1e3)
            overlap=rho/rho0 if rho0>0 else 0
            for seed in SEED_MASSES:
              r=_row('stream',Mms,rau,sk,vk,seed,rho,sig,q)
              r.update(collapse_overlap_fraction=overlap,stream_scale_at_collapse_AU=at/AU,
                  overlap_offset_AU=off/AU,rho_profile_1AU_kgm3=rho1,
                  cluster_survival_prob=np.nan,present_day_if_retained_pass=False,
                  stage1_candidate_if_retained_today=False)
              r['stage1_candidate']=r['phase_space_pass'] and r['f_seed_required']<=1 and overlap>0.1
              rows.append(r)
    return pd.DataFrame(rows)


def scan_torus(g: TorusGrid):
    rows=[]
    Mgrid=np.logspace(np.log10(g.mmin),np.log10(g.mmax),g.mn)
    Wgrid=np.logspace(np.log10(g.wmin),np.log10(g.wmax),g.wn)
    Sgrid=np.linspace(g.smin,g.smax,g.sn)
    Vgrid=np.linspace(0.0,1.0,g.vn)
    omega=solar_omega_1au()
    for Mms in Mgrid:
      M=Mms*M_SUN
      for wAU in Wgrid:
        w=wAU*AU; rho0=torus_peak_density(M,AU,w); fsp=torus_hill_spatial_fraction(w)
        torus_valid=wAU<=0.3
        for sk in Sgrid:
          sig=sk*1e3; epiAU=sig/omega/AU; epi_ok=wAU>=epiAU
          for vk in Vgrid:
            fvel=velocity_eligible_fraction(sig,vk*1e3,g.v_eligible_kms*1e3)
            q=shifted_q(rho0,sig,vk*1e3)
            for seed in SEED_MASSES:
              mu=M*fsp*fvel/seed
              r=dict(branch='torus',Msub_Msun=Mms,rcore_AU=wAU,sigma_input_kms=sk,
                  vrel_kms=vk,seedmass_kg=seed,rho_phase_kgm3=rho0,sigma_phase_ms=sig,
                  Qeff=q,Qeff_Msun_pc3_per_kms3=q_to_msun_pc3_kms3(q),
                  rho_mapped_1AU_kgm3=np.nan,mu_H_mapped=mu,
                  f_seed_required=(math.inf if mu<=0 else F6_MU_REQ/mu),phase_space_pass=mu>=F6_MU_REQ,
                  velocity_eligible_fraction=fvel,hill_spatial_mass_fraction=fsp,
                  epicycle_width_AU=epiAU,epicycle_consistent=epi_ok,torus_thin_approx_valid=torus_valid,
                  total_seed_count=M/seed,cluster_survival_prob=np.nan,present_day_if_retained_pass=False,
                  stage1_candidate_if_retained_today=False)
              r['stage1_candidate']=bool(r['phase_space_pass'] and epi_ok and torus_valid)
              rows.append(r)
    return pd.DataFrame(rows)


def run_grid(g: Grid):
    if g.branch=='mini': return scan_mini(g)
    if g.branch=='stream': return scan_stream(g)
    if g.branch=='both': return pd.concat([scan_mini(g),scan_stream(g)],ignore_index=True,sort=False)
    raise ValueError('Grid supports mini/stream/both; use scan_torus(TorusGrid()) for torus')


def summary(df):
    out={'rows':int(len(df)),'branches':{}}
    for name,s in df.groupby('branch'):
      c=s[s.stage1_candidate]
      entry=dict(rows=int(len(s)),phase_space_pass=int(s.phase_space_pass.sum()),
          stage1_candidate=int(s.stage1_candidate.sum()),
          stage1_candidate_if_retained_today=int(s.stage1_candidate_if_retained_today.sum()),
          candidate_vrel_kms_range=([float(c.vrel_kms.min()),float(c.vrel_kms.max())] if len(c) else None))
      if name=='torus' and len(c): entry['minimum_total_seed_count']=float(c.total_seed_count.min())
      out['branches'][name]=entry
    return out


def plot(df,outdir,seed=1e11):
    import matplotlib.pyplot as plt
    Path(outdir).mkdir(parents=True,exist_ok=True)
    for branch in df.branch.unique():
      s=df[(df.branch==branch)&(df.seedmass_kg==seed)&np.isclose(df.vrel_kms,0)]
      if s.empty: continue
      if branch=='mini': idx,col='rcore_AU','Msub_Msun'
      elif branch=='stream':
        m=np.sort(s.Msub_Msun.unique())[len(s.Msub_Msun.unique())//2]; s=s[np.isclose(s.Msub_Msun,m)]; idx,col='sigma_input_kms','rcore_AU'
      else:
        w=np.sort(s.rcore_AU.unique())[len(s.rcore_AU.unique())//2]; s=s[np.isclose(s.rcore_AU,w)]; idx,col='sigma_input_kms','Msub_Msun'
      p=s.pivot_table(index=idx,columns=col,values='mu_H_mapped',aggfunc='median')
      fig,ax=plt.subplots(figsize=(8,6)); z=np.log10(p.values+1e-300)
      im=ax.imshow(z,origin='lower',aspect='auto'); fig.colorbar(im,ax=ax,label='log10(mu_H)')
      ax.set_title(f'F8a {branch}, seed={seed:.1e} kg'); fig.tight_layout()
      fig.savefig(Path(outdir)/f'f8a_{branch}_seed_{seed:.0e}.png',dpi=180); plt.close(fig)


def q_si_to_msun_pc3_per_kms3(q): return q_to_msun_pc3_kms3(q)
def rho_required_for_mu(seed_mass,mu=F6_MU_REQ): return rho_required(seed_mass,mu)
def shifted_low_velocity_q(rho,sigma,vrel): return shifted_q(rho,sigma,vrel)
def stream_phase_space_at_collapse(M,a0,sigma,vrel,collapse_myr):
    t=collapse_myr*MYR; at=math.sqrt(a0*a0+(sigma*t)**2); off=abs(vrel)*t
    rho=gaussian_density(off,M,at); return at,off,rho,shifted_q(rho,sigma,vrel)
def plummerprofile(rm,Msubkg,rcorem): return plummer_density(rm,Msubkg,rcorem)
def virialsigma(Msubkg,rscalem): return math.sqrt(G*Msubkg/(5.0*rscalem))
def rhosigmaprofile(params):
    M=params['MsubMsun']*M_SUN; a=params['rcoreAU']*AU; model=params.get('model','mini')
    if model in ('torus','comoving_torus'): return {'rho1AU':torus_peak_density(M,AU,a),'sigma1AU':params['sigmasubkms']*1e3}
    return {'rho1AU':plummer_density(AU,M,a),'sigma1AU':plummer_sigma_1d(AU,M,a)}
def muHat1AU(rho1AU,seedmasskg): return mu_from_density(rho1AU,seedmasskg)
def survivalprobability(params,cluster_model='med'):
    return cluster_survival(params['MsubMsun']*M_SUN,params['rcoreAU']*AU,cluster_model)[0]


def rungrid(outcsv,gridparams,seedmasses_kg):
    rows=[]
    Mgrid=np.logspace(np.log10(gridparams['Mmin']),np.log10(gridparams['Mmax']),gridparams['M_N'])
    Sgrid=np.linspace(gridparams['sigmamin'],gridparams['sigmamax'],gridparams['sigma_N'])
    Rgrid=np.logspace(np.log10(gridparams['rminAU']),np.log10(gridparams['rmaxAU']),gridparams['r_N'])
    Vgrid=np.linspace(gridparams['vrelmin'],gridparams['vrelmax'],gridparams['vrel_N'])
    omega=solar_omega_1au()
    for Mms in Mgrid:
      M=Mms*M_SUN
      for sk in Sgrid:
        sig=sk*1e3
        for wAU in Rgrid:
          w=wAU*AU; rho0=torus_peak_density(M,AU,w); fsp=torus_hill_spatial_fraction(w); epiAU=sig/omega/AU
          for vk in Vgrid:
            fvel=velocity_eligible_fraction(sig,vk*1e3,DEFAULT_V_ELIGIBLE_KMS*1e3)
            for seed in seedmasses_kg:
              mu=M*fsp*fvel/seed
              rows.append(dict(MsubMsun=Mms,sigmasubkms=sk,rcoreAU=wAU,vrelkms=vk,
                  seedmasskg=seed,rho1AUkgm3=rho0,sigma1AUms=sig,rhooversigma3=rho0/sig**3,
                  mu_H=mu,velocityEligibleFraction=fvel,hillSpatialMassFraction=fsp,
                  epicycleWidthAU=epiAU,epicycleConsistent=wAU>=epiAU))
    df=pd.DataFrame(rows); Path(outcsv).parent.mkdir(parents=True,exist_ok=True); df.to_csv(outcsv,index=False); return df


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--branch',choices=['mini','stream','both','torus','all'],default='both')
    ap.add_argument('--out',default='results/f8a_grid.csv'); ap.add_argument('--summary',default='results/f8a_summary.json')
    ap.add_argument('--plot-dir',default=None); ap.add_argument('--cluster',choices=CLUSTERS,default='med'); args=ap.parse_args()
    if args.branch=='torus': df=scan_torus(TorusGrid()); cfg=asdict(TorusGrid())
    elif args.branch=='all':
      g=Grid(branch='both',cluster=args.cluster); df=pd.concat([run_grid(g),scan_torus(TorusGrid())],ignore_index=True,sort=False); cfg={'origin':asdict(g),'torus':asdict(TorusGrid())}
    else: g=Grid(branch=args.branch,cluster=args.cluster); df=run_grid(g); cfg=asdict(g)
    print(json.dumps(cfg,indent=2)); Path(args.out).parent.mkdir(parents=True,exist_ok=True); df.to_csv(args.out,index=False)
    sm=summary(df); Path(args.summary).parent.mkdir(parents=True,exist_ok=True); Path(args.summary).write_text(json.dumps(sm,indent=2),encoding='utf-8'); print(json.dumps(sm,indent=2))
    if args.plot_dir:
      for seed in SEED_MASSES: plot(df,args.plot_dir,seed)

if __name__=='__main__': main()
