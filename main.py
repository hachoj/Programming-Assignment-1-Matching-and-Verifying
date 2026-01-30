import argparse
from pathlib import Path

from src.gale_shapely import gale_shapely
from src.io_util import read_preferences, InputError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise ValueError(f"There is no file {input_path}.")

    try:
        n, hospital_prefs, student_prefs = read_preferences(str(input_path))
    except InputError as e:
        print(f"INVALID ({e})")
        raise SystemExit(1)

    match = gale_shapely(n, hospital_prefs, student_prefs)
    for i, s in enumerate(match, start=1):
        print(f"{i} {s}")


if __name__ == "__main__":
    main()
