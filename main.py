import argparse
from pathlib import Path

from src.assignment1.gale_shapely import gale_shapely
from src.assignment1.io_util import InputError, read_preferences
from src.assignment1.verifier import is_stable, one_to_one


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
    print(hospital_prefs)
    print(student_prefs)
    for i, s in enumerate(match, start=1):
        print(f"Hospital {i} matched with Student {s}")
    print(is_stable(all_hospital_prefs=hospital_prefs, all_student_prefs=student_prefs, match=match))


if __name__ == "__main__":
    main()
