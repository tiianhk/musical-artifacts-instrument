from tqdm import tqdm
from pathlib import Path
import argparse, zipfile, rarfile, py7zr

archive_formats = [".zip", ".rar", ".7z"]


def extract_archive(archive_file):
    out_dir = archive_file.parent / archive_file.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        if zipfile.is_zipfile(archive_file):
            with zipfile.ZipFile(archive_file) as zf:
                zf.extractall(out_dir)
        elif rarfile.is_rarfile(archive_file):
            with rarfile.RarFile(archive_file) as rf:
                rf.extractall(out_dir)
        elif archive_file.suffix.lower() == ".7z":
            with py7zr.SevenZipFile(archive_file, mode="r") as sz:
                sz.extractall(out_dir)

        nested = get_archive_files(out_dir)
        if len(nested) > 0:
            print(f"Nested structure found in {archive_file}!")
            for file in nested:
                extract_archive(file)

    except Exception as e:
        print(f"Error extracting archive {archive_file}: {e}")


def get_archive_files(path):
    return [
        f
        for f in Path(path).rglob("*")
        if f.is_file() and f.suffix.lower() in archive_formats
    ]


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    assert out_dir.is_dir(), f"{out_dir} is not a directory."

    files = get_archive_files(out_dir)
    for file in tqdm(files):
        extract_archive(file)
