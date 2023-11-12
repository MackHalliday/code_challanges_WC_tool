import argparse
from pathlib import Path
from model import WCTool

parser = argparse.ArgumentParser(
    prog="code_challenge_wc", description="Rebuilding Linux WC"
)


# optional arugments
parser.add_argument("-c", "--bytes", action="store_true")
parser.add_argument("-l", "--lines", action="store_true")
parser.add_argument("-w", "--words", action="store_true")
parser.add_argument("-m", "--characters", action="store_true")

# positional argument
parser.add_argument("path")


def main():
    args = parser.parse_args()
    file_path = Path(args.path)

    if file_path:
        output = WCTool(file_path, args).run_command()
        return print(output)


if __name__ == "__main__":
    main()
