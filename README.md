Script for downloading standalone virtual instruments from [musical-artifacts.com](https://musical-artifacts.com). Metadata was fetched, filtered, and stored in `musical_artifacts.json` using the website's [API](https://github.com/lfzawacki/musical-artifacts/wiki/API-Documentation) on 2025-10-26. The lastest instrument ID is 7254 ([this instrument](https://musical-artifacts.com/artifacts/7254)), which was uploaded on the same date.

### Usage

To download:
```
python download.py --out_dir path/to/out_dir
```
 - If `--out_dir` is not given, the default output directory is `data/` .
 - Server errors may occur and are printed for unsuccessful downloads. You can safely re-run the script later with the same output directory, which will skip previously successful downloads and retry the failed ones.
 - The total download is ~93G and takes ~10 hours.
 - The downloaded files are mainly `*.sf2`, but might be archives, `*.sf3`, or `*.sfz` .

To unpack the archives ( `*.zip`, `*.rar`, and `*.7z` ):
```
python unpack.py --out_dir path/to/out_dir
```
 - Use the same out_dir as download.
 - Nested structures will be unpacked recursively.
 - The total size comes to ~147G.

### Licenses
All instruments are under one of the following licenses:
 - Public Domain
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
