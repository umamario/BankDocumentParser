import argparse
import os

import pandas as pd

from parsers.bank1 import Bank1Parser
from parsers.bank2 import Bank2Parser
from parsers.bank3 import Bank3Parser

bank_class_map = {
    "bank1": Bank1Parser,
    "bank2": Bank2Parser,
    "bank3": Bank3Parser
}


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("--input_dir", required=True, help="Path to the directory containing the report files")
    parser.add_argument("--output_file", required=False, help="Path to the output file", default="output.csv")

    return parser.parse_args()


def main():
    arguments = parse_args()
    all_movements = []
    if not os.path.isdir(arguments.input_dir):
        raise Exception(f"Directory {arguments.input_dir} does not exist")

    for file in os.listdir(arguments.input_dir):
        filename, _ = os.path.splitext(file)
        parser_class = bank_class_map.get(filename)  # the filename is used as the bank identifier

        if parser_class:
            file_path = f"{arguments.input_dir}/{file}"
            movements = parser_class(input_file_path=file_path).generate_report()
            all_movements += movements

    df = pd.DataFrame.from_records([vars(movement) for movement in all_movements])
    df.to_csv(arguments.output_file)


if __name__ == '__main__':
    main()
