import argparse
import sys
from typing import List, Tuple
from status_code_checker.status_code_checker import explain_status_code

# ASCII escape codes for formatting output
BOLD = "\033[1m"
RESET = "\033[0m"


def parse_cli_args(argv: List[str]) -> Tuple[List[int], List[str]]:
    parser = argparse.ArgumentParser(
        prog="Status Code Checker",
        description="Returns an explanation of the http status codes provided to the tool.",
    )

    # Accept zero or more positional args; we'll do lenient parsing ourselves
    parser.add_argument("values", nargs="*", help="Values to parse as integers")
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
        print(
            f"Discarded non-integer {'values' if len(invalid) > 1 else 'value' }: {', '.join(invalid)}"
        )

    explained = explain_status_code(ints)
    explained_indented = [f"    {line}" for line in explained]

    print(
        "",
        (
            f"{BOLD}Status Code Explanations:{RESET}"
            if len(explained) > 1
            else f"{BOLD}Status Code Explanation:{RESET}"
        ),
        *explained_indented,
        "",
        sep="\n",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
