# Musical Artifacts Instrument

Python scripts for downloading standalone virtual instruments from [musical-artifacts.com](https://musical-artifacts.com) . \
Metadata was fetched, filtered, and stored in `metadata.json` using the website's [API](https://github.com/lfzawacki/musical-artifacts/wiki/API-Documentation) on 2025-10-26. \
It contains data hosted on 2,629 webpages. Check the [first](https://musical-artifacts.com/artifacts/8) and the [last](https://musical-artifacts.com/artifacts/7254) . The upload period spans from 2015-07-29 to 2025-10-26. \
Data for each item contains at least one file in `.sf2`, `.sf3` , or `.sfz` format. All licenses are listed [here](#Licenses).

## Environment

1. Install [uv](https://github.com/astral-sh/uv) if you don't have it. Verify by running `which uv` .
2. Install [unrar](https://www.rarlab.com) if you don't have it. Verify by running `which unrar` . Note: if you don’t have sudo privileges on Linux and want to install it, you can follow the instructions [here](https://www.linuxfromscratch.org/blfs/view/svn/general/unrar.html) to build from source, and make the executable available in PATH (e.g., by moving it to `~/.local/bin` ).
3. Clone this repository, open its directory, and sync the environment:
```bash
git clone https://github.com/tiianhk/musical-artifacts-instrument.git
cd musical-artifacts-instrument
uv sync
```

## Usage

To download:
```bash
uv run python download.py --out_dir path/to/out_dir
```
 - If `--out_dir` is not given, the default output directory is `data/` .
 - Server errors may occur and are printed for unsuccessful downloads. You can safely re-run the script later with the same output directory, which will skip previously successful downloads and retry the failed ones.
 - The total download is ~93G and takes ~10 hours.
 - The downloaded files are mainly `*.sf2` , but might be `*.sf3` , `*.sfz` , or archives.

To unpack the archives ( `*.zip` , `*.rar` , and `*.7z` ):
```bash
uv run python unpack.py --out_dir path/to/out_dir
```
 - Use the same `out_dir` as download.
 - Nested structures will be unpacked recursively.
 - The total size comes to ~147G.

To find and tag duplicates:
```bash
uv run python deduplicate.py --out_dir path/to/out_dir
```
 - Use the same `out_dir` as download and unpack.
 - It checks all `*.sf2`, `*.sf3` , and `*.sfz` files.
 - For files that are duplicates of each other, it keeps one of them as is and tags the others as duplicates by adding `.duplicate` to their filenames.

## Licenses

All instruments are either in the public domain or under one of the following licenses:
 - Creative Commons Attribution 3.0
 - Creative Commons Attribution 4.0
 - Creative Commons Attribution-ShareAlike 3.0
 - Creative Commons Attribution-ShareAlike 4.0
 - Creative Commons Attribution-NonCommercial 3.0
 - Creative Commons Attribution-NonCommercial 4.0
 - Creative Commons Attribution-NonCommercial-ShareAlike 4.0
 - GNU General Public License V1
 - GNU General Public License V2
 - GNU General Public License V3
 - Free Art License v1.3
 - Do What The Fuck You Want To Public License v2

## Synthesizers

For audio synthesis in Python, it is recommanded to use [pyfluidsynth](https://github.com/nwhitehead/pyfluidsynth/tree/master) for `.sf2` and `.sf3` files, and [pysfizz](https://github.com/tiianhk/pysfizz) for `.sfz` files.
