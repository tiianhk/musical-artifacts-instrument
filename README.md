Script for downloading standalone virtual instruments (not synthesizer presets) from [musical-artifacts.com](https://musical-artifacts.com) using its public API.

### Usage
```
python download.py --out_dir path/to/out_dir
```
 - If `--out_dir` is not given, the default output directory is `data/`
 - The downloaded files are mainly `*.sf2`, but might be archives, `*.sf3`, or `*.sfz`
 - Server errors may occur and are printed for unsuccessful downloads. You can safely re-run the script, which will skip previously successful downloads and retry the failed ones.

### Licenses
All instruments are under one of the following licenses:
 - Public Domain
 - Creative Commons Attribution 4.0
 - Creative Commons Attribution-ShareAlike 4.0
 - Creative Commons Attribution-NonCommercial 4.0
 - Creative Commons Attribution-NonCommercial-ShareAlike 4.0
 - GNU General Public License V1
 - GNU General Public License V2
 - GNU General Public License V3
 - Free Art License v1.3
 - Do What The Fuck You Want To Public License v2
 - Creative Commons Attribution 3.0
 - Creative Commons Attribution-ShareAlike 3.0
 - Creative Commons Attribution-NonCommercial 3.0
