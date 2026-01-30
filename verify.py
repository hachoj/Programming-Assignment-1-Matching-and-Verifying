import argparse
from pathlib import Path

from assignment1.io_util import InputError, read_preferences
from assignment1.verifier import is_stable, one_to_one


def read_matching(path, n):
    raw = Path(path).read_text(encoding="utf-8").splitlines()
    pairs = []
    for line in raw:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Each output line must have two integers.")
        h = int(parts[0])
        s = int(parts[1])
        pairs.append((h, s))

    if len(pairs) != n:
        raise ValueError("Wrong number of matching lines.")

    match = [0] * n
    seen_h = set()
    seen_s = set()

    for h, s in pairs:
        if h < 1 or h > n or s < 1 or s > n:
            raise ValueError("Out-of-range id in matching.")
        if h in seen_h:
            raise ValueError("Duplicate hospital in matching.")
        if s in seen_s:
            raise ValueError("Duplicate student in matching.")
        seen_h.add(h)
        seen_s.add(s)
        match[h - 1] = s

    return match


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("output_path")
    args = parser.parse_args()

    try:
        n, hospital_prefs, student_prefs = read_preferences(args.input_path)
    except InputError as e:
        print(f"INVALID ({e})")
        raise SystemExit(1)

    out_path = Path(args.output_path)
    if not out_path.exists():
        print("INVALID (Output file not found.)")
        raise SystemExit(1)

    try:
        match = read_matching(out_path, n)
    except Exception as e:
        print(f"INVALID ({e})")
        raise SystemExit(1)

    if not one_to_one(match):
        print("INVALID (Not one-to-one.)")
        raise SystemExit(1)

    if is_stable(hospital_prefs, student_prefs, match):
        print("VALID STABLE")
    else:
        print("UNSTABLE")


if __name__ == "__main__":
    main()
