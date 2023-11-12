import argparse
from pathlib import Path
from wc_tool import WCTool

parser = argparse.ArgumentParser(
    prog="code_challenge_wc", description="Rebuilding Linux WC"
)

# positional argument
parser.add_argument("path")

# optional arugments
parser.add_argument("-c", "--bytes", action="store_true")
parser.add_argument("-l", "--lines", action="store_true")
parser.add_argument("-w", "--words", action="store_true")
parser.add_argument("-m", "--characters", action="store_true")


def main():
    file_path_arg = parser.parse_args(
        [
            "path",
        ]
    )
    file_path = Path(file_path_arg.path)

    optional_args = parser.parse_known_args(["-c", "-l", "-w", "-m"])

    if file_path:
        return WCTool(file_path, optional_args)
