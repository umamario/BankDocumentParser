# Bank document parser

This script parses multiple transaction reports on CSV/JSON to create a unified CSV document.

## Usage
Install the requirement listed on requirement.txt
```bash
pip3 install -r requirement.txt
```
Run the python script main.py as explained below
```bash
python main.py [-h] --input_dir INPUT_DIR [--output_file OUTPUT_FILE]
Arguments:
  -h, --help            show the help message and exit
  --input_dir INPUT_DIR
                        Path to the directory containing the report files
  --output_file OUTPUT_FILE
                        Path to the output file
```
