import os
import csv


def read_csv_files(paths: str) -> list[dict[str, str]]:
    data = []
    for path in paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"file not found: {path}")
        if not path.lower().endswith(".csv"):
            raise ValueError(f"files must be with csv extension")

        with open(path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

    return data
