#!/usr/bin/env python3
"""Download the small, official Zenodo stage-1 artifacts with checksum verification.

Usage:
  python experiments/standing_peg_in_hole/fetch_stage1.py --dest /path/to/data/standing_peg_in_hole
  python experiments/standing_peg_in_hole/fetch_stage1.py --dest /path/to/data/standing_peg_in_hole --include-model

Does not unpack or execute third-party code. Downloads no large evaluation/data archives.
"""
import argparse
import hashlib
import urllib.request
from pathlib import Path

BASE = "https://zenodo.org/records/21768344/files/"
FILES = {
    "README.md": "8b6daad23a4a929ee6478c7c4e584524",
    "LICENSE.txt": "334af90c0b2929dbcd994c53a3a70499",
    "SHA256SUMS.txt": "62a4f08242b982b7d1603b519ac5fa64",
    "code_and_assets.zip": "7002022151e93a8782abe721991ac15d",
    "model_smolvla_40k.zip": "19c093898cd9305f254317e9840e0de4",
}

def md5(path):
    digest = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", required=True, type=Path)
    parser.add_argument("--include-model", action="store_true")
    args = parser.parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    for name, expected in FILES.items():
        if name == "model_smolvla_40k.zip" and not args.include_model:
            continue
        target = args.dest / name
        if target.exists() and md5(target) == expected:
            print("OK (cached):", target)
            continue
        partial = target.with_name(target.name + ".part")
        print("Downloading:", name, flush=True)
        urllib.request.urlretrieve(BASE + name + "?download=1", partial)
        actual = md5(partial)
        if actual != expected:
            partial.unlink(missing_ok=True)
            raise RuntimeError(f"Checksum mismatch for {name}: {actual} != {expected}")
        partial.replace(target)
        print("Verified:", target, flush=True)

if __name__ == "__main__":
    main()
