#!/usr/bin/env python3
"""Build a deterministic skill bundle and SHA-256 checksum."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def included_files() -> list[Path]:
    roots = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHANGELOG.md",
        ROOT / "VERSION",
        ROOT / "install.sh",
    ]
    roots.extend(path for path in (ROOT / "skills").rglob("*") if path.is_file())
    return sorted(roots, key=lambda path: path.relative_to(ROOT).as_posix())


def add_file(archive: zipfile.ZipFile, path: Path, prefix: str) -> None:
    relative = path.relative_to(ROOT).as_posix()
    info = zipfile.ZipInfo(f"{prefix}/{relative}", FIXED_TIMESTAMP)
    # Store bytes without compression so archives remain identical across
    # platforms with different zlib versions.
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    executable = relative == "install.sh" or relative.endswith(".py")
    mode = 0o755 if executable else 0o644
    info.external_attr = (0o100000 | mode) << 16
    archive.writestr(info, path.read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="dist")
    args = parser.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if re.fullmatch(r"\d+\.\d+\.\d+", version) is None:
        raise SystemExit("error: VERSION must contain a semantic version")

    output_dir = (ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_name = f"run-ab-experiments-bundle-v{version}.zip"
    archive_path = output_dir / archive_name
    prefix = f"run-ab-experiments-skill-v{version}"

    with zipfile.ZipFile(archive_path, "w") as archive:
        for path in included_files():
            add_file(archive, path, prefix)

    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    checksum_path = archive_path.with_suffix(archive_path.suffix + ".sha256")
    checksum_path.write_text(f"{digest}  {archive_name}\n", encoding="utf-8")
    os.chmod(archive_path, 0o644)
    os.chmod(checksum_path, 0o644)
    print(archive_path.relative_to(ROOT))
    print(checksum_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
