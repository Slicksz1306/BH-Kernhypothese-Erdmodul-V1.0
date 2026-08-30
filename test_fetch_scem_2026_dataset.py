from pathlib import Path
import tempfile
import unittest
import zipfile

from fetch_scem_2026_dataset import EXPECTED_MD5, inventory_bm, md5sum, safe_extract


class TestSCEMDatasetAcquisition(unittest.TestCase):
    def test_md5sum(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.bin"
            p.write_bytes(b"abc")
            self.assertEqual(md5sum(p), "900150983cd24fb0d6963f7d28e17f72")

    def test_expected_zenodo_checksum_is_pinned(self):
        self.assertEqual(EXPECTED_MD5, "2ea938e999278417dc3dbec378a06651")

    def test_safe_extract_and_bm_inventory(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            z = root / "models.zip"
            with zipfile.ZipFile(z, "w") as zf:
                zf.writestr("MAP/SCEM_map.bm", "dummy")
                zf.writestr("bounds/vp.txt", "dummy")
            dest = root / "models"
            safe_extract(z, dest)
            self.assertEqual(
                [p.relative_to(dest).as_posix() for p in inventory_bm(dest)],
                ["MAP/SCEM_map.bm"],
            )

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            z = root / "bad.zip"
            with zipfile.ZipFile(z, "w") as zf:
                zf.writestr("../escape.bm", "bad")
            with self.assertRaises(ValueError):
                safe_extract(z, root / "out")


if __name__ == "__main__":
    unittest.main()
