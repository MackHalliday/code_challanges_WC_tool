import subprocess
import pytest


class TestWCTool:
    ccwc_file = (
        "/Users/mack/coding/coding_challenges/write_your_own_wc_tool/ccwc/ccwc.py"
    )

    def test_can_return_number_of_bytes_in_file(self):
        print(self.ccwc_file)
        result = subprocess.check_output(
            ["python3", self.ccwc_file, "-c", "tests/test.txt"], universal_newlines=True
        )
        assert result == "342190 tests/test.txt\n"

    def test_can_return_number_of_lines_in_file(self):
        result = subprocess.check_output(
            ["python3", self.ccwc_file, "-l", "tests/test.txt"], universal_newlines=True
        )

        assert result == "7145 tests/test.txt\n"

    def test_can_return_number_of_words_in_file(self):
        result = subprocess.check_output(
            ["python3", self.ccwc_file, "-w", "tests/test.txt"], universal_newlines=True
        )

        assert result == "58164 tests/test.txt\n"

    def test_can_return_number_of_characters_in_file(self):
        result = subprocess.check_output(
            ["python3", self.ccwc_file, "-m", "tests/test.txt"], universal_newlines=True
        )

        assert result == "339292 tests/test.txt\n"

    def test_can_return_bytes_line_word_as_default_option(self):
        result = subprocess.check_output(
            ["python3", self.ccwc_file, "tests/test.txt"], universal_newlines=True
        )

        assert result == "7145  58164  339292 tests/test.txt\n"

    def test_error_handling_for_invalid_input(self):
        pass
        result = ""

        assert (
            result == "ValueError: Invalid command. Expected: '-c, -l, -w, -m, or None"
        )
