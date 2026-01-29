import argparse
import os
from pathlib import Path

from src.gale_shapely import gale_shapely


def main():
    parser = argparse.ArgumentParser(
        prog="Gale Shapely Test",
        description="Takes paths of input spec and optionally output spec to ... TODO",
    )
    parser.add_argument(
        "-i",
        "--input",
        action="store",
        type=str,
        required=True,
        help="Path to input (*.in) file",
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        type=str,
        help="OPTIONAL path to output (*.out) file",
    )
    args = parser.parse_args()

    input_path = args.input
    input_path = Path(input_path)
    if not os.path.exists(input_path):
        raise ValueError(f"There is no file {input_path}.")

    input_file = open(input_path)
    input_text = input_file.read()

    output_path = args.output
    if output_path is not None:
        output_path = Path(output_path)
        if not os.path.exists(output_path):
            raise ValueError(f"There is no file {output_path}.")

        output_file = open(output_path)
        output_text = output_file.read()

    # --- temp print before something is actually implemented ---
    print(gale_shapely())
    print(input_text)
    if output_path is not None:
        print("-" * 30)
        print(output_text)


if __name__ == "__main__":
    main()
