import argparse

from src.utils.csv_reader import read_csv_files
from src.reports.reports import AverageRatingReport


REPORT_TYPES = {
    "average-rating": AverageRatingReport(),
}


def main():
    parser = argparse.ArgumentParser(description="brand analysis scriptp")
    parser.add_argument(
        "--files", nargs="+", required=True, help="csv files paths"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=REPORT_TYPES.keys(),
        help="report types",
    )

    args = parser.parse_args()

    data = read_csv_files(args.files)

    report = REPORT_TYPES[args.report]
    result = report.generate(data)
    report.display(result)


if __name__ == "__main__":
    main()
