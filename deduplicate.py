"""
Adapted from https://gist.github.com/tfeldmann/fc875e6630d11f2256e746f67a09c1ae
"""
import hashlib
from collections import defaultdict
from pathlib import Path
import argparse


suffixes = [".sf2", ".sf3", ".sfz"]


def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes."""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(filepath, first_chunk_only=False, hash_algo=hashlib.sha1):
    """Compute hash of file (optionally only first 1024 bytes)."""
    hashobj = hash_algo()
    with filepath.open("rb") as f:
        if first_chunk_only:
            hashobj.update(f.read(1024))
        else:
            for chunk in chunk_reader(f):
                hashobj.update(chunk)
    return hashobj.digest()


def check_for_duplicates(path):
    files_by_size = defaultdict(list)
    files_by_small_hash = defaultdict(list)
    files_by_full_hash = defaultdict(list)

    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in suffixes:
            continue
        try:
            file_path = file_path.resolve()
            file_size = file_path.stat().st_size
        except Exception as e:
            print(f"failed to resolve or get size for {file_path}: {e}")
            continue
        files_by_size[file_size].append(file_path)

    # For all files with the same file size, get their hash on the first 1024 bytes
    for file_size, files in files_by_size.items():
        if len(files) < 2:
            continue
        for file_path in files:
            try:
                small_hash = get_hash(file_path, first_chunk_only=True)
            except Exception as e:
                print(f"failed to get hash for {file_path}: {e}")
                continue
            files_by_small_hash[(file_size, small_hash)].append(file_path)

    # For files with the same small hash, check full file hash
    for files in files_by_small_hash.values():
        if len(files) < 2:
            continue
        for file_path in files:
            try:
                full_hash = get_hash(file_path, first_chunk_only=False)
            except Exception as e:
                print(f"failed to get hash for {file_path}: {e}")
                continue
            files_by_full_hash[full_hash].append(file_path)

    # Keep one duplicate and rename the others
    group_cnt = 0
    for files in files_by_full_hash.values():
        if len(files) < 2:
            continue
        print(f"Duplicate group / {group_cnt}:")
        print(f" - {files[0]}")
        for file_path in files[1:]:
            new_path = file_path.with_name(file_path.name + ".duplicate")
            try:
                file_path.rename(new_path)
                print(f" - {new_path} (renamed)")
            except Exception as e:
                print(f" - {file_path} (failed to rename: {e})")
        print("\n")
        group_cnt += 1
    if group_cnt == 0:
        print("No duplicates!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    assert out_dir.is_dir(), f"{out_dir} is not a directory."
    
    check_for_duplicates(out_dir)
