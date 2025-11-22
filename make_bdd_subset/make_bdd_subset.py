#!/usr/bin/env python3
"""
Create a smaller BDD100K subset using config.yaml

Usage:
    python make_bdd_subset.py --config config.yaml
"""

import argparse
import json
import random
import shutil
import yaml
from pathlib import Path


# ----------------------------
# Argument Parsing
# ----------------------------
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        type=Path,
        help="YAML config file path"
    )

    return parser.parse_args()


# ----------------------------
# Load YAML Config
# ----------------------------
def load_config(config_path: Path):
    with config_path.open("r") as f:
        return yaml.safe_load(f)


# ----------------------------
# Utility functions
# ----------------------------
def normalize(s):
    return s.lower().strip() if isinstance(s, str) else None


def match_attr(attr_value, wanted):
    if wanted is None:
        return True
    wanted = normalize(wanted)
    if wanted == "any":
        return True
    return normalize(attr_value) == wanted


def find_image_for_label(images_dir: Path, stem: str):
    for ext in [".jpg", ".jpeg", ".png"]:
        p = images_dir / f"{stem}{ext}"
        if p.exists():
            return p
    return None


# ----------------------------
# Collect filtered candidates
# ----------------------------
def collect_candidates(split, images_root, labels_root, weather, scene, timeofday):
    labels_dir = labels_root / split
    images_dir = images_root / split

    candidates = []

    json_files = sorted(labels_dir.glob("*.json"))
    print(f"[{split}] 전체 label 파일: {len(json_files)}")

    for jpath in json_files:
        with jpath.open("r") as f:
            data = json.load(f)

        attrs = data.get("attributes", {})
        w = attrs.get("weather")
        s = attrs.get("scene")
        t = attrs.get("timeofday")

        if not match_attr(w, weather):
            continue
        if not match_attr(s, scene):
            continue
        if not match_attr(t, timeofday):
            continue

        stem = jpath.stem
        img_path = find_image_for_label(images_dir, stem)
        if img_path:
            candidates.append((stem, jpath, img_path))

    print(f"[{split}] 필터 통과: {len(candidates)}")
    return candidates


# ----------------------------
# Sample & Copy
# ----------------------------
def sample_and_copy(split, candidates, requested_num, out_root):
    out_labels = out_root / "labels" / split
    out_images = out_root / "images" / split
    out_labels.mkdir(parents=True, exist_ok=True)
    out_images.mkdir(parents=True, exist_ok=True)

    total = len(candidates)
    if total == 0:
        print(f"[{split}] 후보 없음.")
        return 0

    if requested_num <= 0 or requested_num > total:
        num = total
    else:
        num = requested_num

    random.shuffle(candidates)
    selected = candidates[:num]

    print(f"[{split}] {total} 중 {num} 샘플 선택")

    for stem, jpath, img_path in selected:
        shutil.copy2(jpath, out_labels / f"{stem}.json")
        shutil.copy2(img_path, out_images / img_path.name)

    return num


# ----------------------------
# Main
# ----------------------------
def main():
    args = parse_args()

    # Load YAML
    if not args.config:
        raise ValueError("--config 파일을 반드시 지정해야 합니다.")

    config = load_config(args.config)
    print("=== Loaded Config ===")
    print(config)

    images_root = Path(config["paths"]["images_root"])
    labels_root = Path(config["paths"]["labels_root"])
    output_root = Path(config["paths"]["output_root"])

    weather = config["filter"]["weather"]
    scene = config["filter"]["scene"]
    timeofday = config["filter"]["timeofday"]

    num_train = config["samples"]["num_train"]
    num_val = config["samples"]["num_val"]
    num_test = config["samples"]["num_test"]

    seed = config.get("seed", 42)
    random.seed(seed)

    splits = {
        "train": num_train,
        "val": num_val,
        "test": num_test,
    }

    for split, req_num in splits.items():
        candidates = collect_candidates(
            split,
            images_root,
            labels_root,
            weather,
            scene,
            timeofday,
        )

        sample_and_copy(split, candidates, req_num, output_root)


if __name__ == "__main__":
    main()
