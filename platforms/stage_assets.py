"""Stage files from a licensed installation after verifying the LAN build manifest."""
import argparse
import hashlib
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path)
parser.add_argument("runtime", type=Path)
args = parser.parse_args()
manifest = Path(__file__).with_name("assets.sha256")
copies = []
for line in manifest.read_text().splitlines():
    digest, name = line.split("  ", 1)
    target = args.runtime / name
    # Deployment generates generalsx.big and may supply other matching files.
    candidates = (target, args.source / name)
    if name == "generalsx.big":
        candidates += (Path(__file__).with_name(name),)
    for candidate in candidates:
        if candidate.is_file():
            with candidate.open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() == digest:
                    if candidate != target:
                        copies.append((candidate, target))
                    break
    else:
        parser.exit(1, f"Missing or different file: {name}\n")
for source, target in copies:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
print(f"Assets verified. Copied {len(copies)} files.")
