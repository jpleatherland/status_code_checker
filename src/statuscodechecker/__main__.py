import argparse
import sys
from typing import List, Tuple
from status_code_checker import explain_status_code

def parse_cli_args(argv: List[str]) -> Tuple[List[int], List[str]]:
    parser = argparse.ArgumentParser(
        prog="Status Code Checker",
        description="Returns an explanation of the http status codes provided to the tool."
    )

    # Accept zero or more positional args; we'll do lenient parsing ourselves
    parser.add_argument(
        "values",
        nargs="*",
        help="Values to parse as integers"
    )
    args = parser.parse_args(argv[1:])

    ints: List[int] = []
    invalid: List[str] = []
    for v in args.values:
        try:
            ints.append(int(v))
        except (ValueError, TypeError):
            invalid.append(v)
    return ints, invalid

def main() -> int:
    if len(sys.argv) < 2:
        print("No arguments provided.")
        return 1

    ints, invalid = parse_cli_args(sys.argv)

    if invalid:
        print(f"Discarded non-integer values: {', '.join(invalid)} (integers are required)")

    explained = explain_status_code(ints)

    formatted = format_explanations(explained)

    print(ints)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
