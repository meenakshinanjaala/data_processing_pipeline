import csv
import json
import logging
import argparse
from pathlib import Path

logging.basicConfig(
level=logging.INFO,
format="%(levelname)s: %(message)s"
)

def process_data(input_file, output_file):
input_path = Path(input_file)
output_path = Path(output_file)

if not input_path.exists():
    logging.error("Input file not found: %s", input_file)
    return False

cleaned_data = []

try:
    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            logging.error("Input CSV is empty or has no header.")
            return False

        for row in reader:
            cleaned_row = {}

            for key, value in row.items():
                if key is not None:
                    cleaned_row[key.strip()] = (
                        value.strip() if value is not None else ""
                    )

            if not any(cleaned_row.values()):
                continue

            cleaned_data.append(cleaned_row)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(cleaned_data, file, indent=4, ensure_ascii=False)

    logging.info("Processing completed successfully.")
    logging.info("Records processed: %d", len(cleaned_data))
    logging.info("Output saved to: %s", output_file)
    return True

except (OSError, csv.Error, json.JSONDecodeError) as error:
    logging.error("Error processing data: %s", error)
    return False

def main():
parser = argparse.ArgumentParser(
description="Clean CSV data and convert it to JSON."
)

parser.add_argument(
    "input_file",
    nargs="?",
    default="input.csv",
    help="Path to the input CSV file"
)

parser.add_argument(
    "-o",
    "--output",
    default="output.json",
    help="Path to the output JSON file"
)

args = parser.parse_args()
process_data(args.input_file, args.output)

if name == "main":
main()