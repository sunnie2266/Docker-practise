import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation

parser = argparse.ArgumentParser(description="Analyse expenses from a CSV file without a web server.")
parser.add_argument("csv_file", nargs="?", default="expenses.csv", help="CSV to analyse")
args = parser.parse_args()

totals = defaultdict(Decimal)
transactions = 0
try:
    with open(args.csv_file, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            category = row["Category"].strip() or "Uncategorised"
            amount = Decimal(row["Amount"])
            totals[category] += amount
            transactions += 1
except (OSError, KeyError, InvalidOperation) as exc:
    parser.exit(1, f"Could not analyse CSV: {exc}\n")

print("=== DOCKER EXPENSE ANALYSER ===")
print(f"Analysed {transactions} transactions from {args.csv_file}\n")
for category, amount in sorted(totals.items()):
    print(f"{category:<16} ${amount:>8.2f}")
print("-" * 27)
print(f"{'TOTAL':<16} ${sum(totals.values(), Decimal('0')):>8.2f}")
print("Completed with Python inside a non-web Docker container.")
