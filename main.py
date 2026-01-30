import argparse
from pathlib import Path

from assignment1.gale_shapely import gale_shapely
from assignment1.io_util import InputError, read_preferences
from assignment1.verifier import is_stable, one_to_one


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output")
    parser.add_argument("-v", "--verify", action='store_false')
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
    match_text = ""
    for i, s in enumerate(match, start=1):
        if i != len(match):
            match_text += f"{i} {s}\n"
        else:
            match_text += f"{i} {s}"

    
    if args.output is not None:
        output_path = Path(args.output)
        if not output_path.exists():
            raise ValueError(f"There is no file {output_path}.")
        output_file = open(output_path)
        output_text = output_file.read()
        
        if output_text == match_text:
            print("Given outputs and gale_shapely output match!")
        else:
            print(f"Given outputs: {output_text} does not match gale shapely output: {match_text}")
    else:
        print(f"No example outputs given")
        print(f"Gale Shapely results: \n{match_text}")
    print('-' * 30)
    print('Gale Shapely output:')
    for hospital, student in enumerate(match, start=1):
        print(hospital, student)
    
    if args.verify is not None:
        print(f"Running one-to-one check...")
        if one_to_one(match):
            print("VALID")
        else:
            print("INVALID")
        print('-' * 30)
        print(f"Running stability check...")
        if is_stable(hospital_prefs, student_prefs, match):
            print("STABLE")
        else:
            print("UNSTABLE")



if __name__ == "__main__":
    main()
