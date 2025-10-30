from tqdm import tqdm
from pathlib import Path
import argparse, time, json, requests

licenses = [
    "by",
    "public",
    "by-sa",
    "gpl-v2",
    "gpl-v3",
    "gpl",
    "by-nc-sa",
    "falv13",
    "wtfpl",
    "by-nc",
    "by-3",
    "by-sa-3",
    "by-nc-3",
]

formats = ["sf2", "sf3", "sfz", ".sf2", ".sf3", ".sfz"]

suffixes = [".sf2", ".sf3", ".sfz", ".zip", ".rar", ".7z"]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open("musical_artifacts.json", "r") as f:
        musical_artifacts = json.load(f)

    downloaded = [str(p.name) for p in out_dir.iterdir()]

    for item in tqdm(musical_artifacts):
        assert Path(item["file"]).suffix.lower() in suffixes
        assert item["license"] in licenses
        assert set(item["formats"]) & set(formats)
        start_time = time.time()
        if str(item["id"]) in downloaded:
            continue
        try:
            response = requests.get(item["file"])
            response.raise_for_status()
        except Exception as e:
            print(f"error for {item['id']}: {e}")
            continue
        path = Path(item["file"])
        path = out_dir / str(item["id"]) / path.name
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(response.content)
        end_time = time.time()
        if end_time - start_time < 1:
            time.sleep(1)
