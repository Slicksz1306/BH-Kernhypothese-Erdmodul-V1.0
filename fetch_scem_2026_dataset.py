"""Safe acquisition helper for the Munch et al. (2026) SCEM/P-PEM dataset.

This helper only downloads, verifies and inventories the public Zenodo archive.
It does not promote SCEM values into the H0 solver and performs no scientific
inference by itself.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import shutil
import urllib.request
import zipfile

ZENODO_RECORD = "https://zenodo.org/records/18386410"
MODELS_URL = f"{ZENODO_RECORD}/files/models.zip?download=1"
EXPECTED_MD5 = "2ea938e999278417dc3dbec378a06651"


def md5sum(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def download_file(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "SL-BH-Kernhypothese-research-audit/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as out:
        shutil.copyfileobj(response, out)


def safe_extract(zip_path: Path, destination: Path) -> list[Path]:
    """Extract a ZIP while rejecting absolute/path-traversal members."""
    destination.mkdir(parents=True, exist_ok=True)
    dest_resolved = destination.resolve()
    extracted: list[Path] = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            target = (destination / info.filename).resolve()
            if target != dest_resolved and dest_resolved not in target.parents:
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(destination)
        for info in zf.infolist():
            if not info.is_dir():
                extracted.append(destination / info.filename)
    return extracted


def inventory_bm(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.bm") if p.is_file())


def fetch_scem(output_dir: Path, force: bool = False) -> dict:
    output_dir = output_dir.resolve()
    archive = output_dir / "models.zip"
    extracted_dir = output_dir / "models"

    if archive.exists() and not force:
        digest = md5sum(archive)
        if digest != EXPECTED_MD5:
            raise RuntimeError(
                f"existing archive checksum mismatch: {digest} != {EXPECTED_MD5}; "
                "use --force only after verifying the source"
            )
    else:
        if archive.exists():
            archive.unlink()
        download_file(MODELS_URL, archive)
        digest = md5sum(archive)
        if digest != EXPECTED_MD5:
            archive.unlink(missing_ok=True)
            raise RuntimeError(
                f"download checksum mismatch: {digest} != {EXPECTED_MD5}"
            )

    if extracted_dir.exists() and force:
        shutil.rmtree(extracted_dir)
    if not extracted_dir.exists():
        safe_extract(archive, extracted_dir)

    bm_files = inventory_bm(extracted_dir)
    return {
        "record": ZENODO_RECORD,
        "archive": str(archive),
        "md5": md5sum(archive),
        "verified": md5sum(archive) == EXPECTED_MD5,
        "bm_file_count": len(bm_files),
        "bm_files": [str(p.relative_to(extracted_dir)) for p in bm_files],
        "scientific_status": "DATA_ACQUISITION_ONLY / NUMERICAL_INGESTION_NOT_YET_PERFORMED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("external_data/scem_2026"),
        help="destination for verified external SCEM data",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    result = fetch_scem(args.output_dir, force=args.force)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
