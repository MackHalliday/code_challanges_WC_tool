import subprocess
import pytest


class TestWCTool:
    def test_can_return_number_of_bytes_in_file(self):
        result_bytes = subprocess.check_output(
            ["python3", "ccwc/ccwc.py", "-c", "tests/test.txt"], universal_newlines=True
        )
        assert result_bytes == "342190 tests/test.txt\n"

    @pytest.mark.skip()
    def test_can_return_number_of_lines_in_file(self):
        pass
        result = ""

        assert result == "7145 test.txt"

    @pytest.mark.skip()
    def test_can_return_number_of_words_in_file(self):
        pass
        result = ""

        assert result == "58164 test.txt"

    @pytest.mark.skip()
    def test_can_return_number_of_characters_in_file(self):
        pass
        result = ""

        assert result == "339292 test.txt"

    @pytest.mark.skip()
    def test_can_return_bytes_line_word_as_default_option(self):
        pass
        result = ""

        assert result == "7145  58164  342190 test.txt"

    @pytest.mark.skip()
    def test_error_handling_for_invalid_input(self):
        pass
        result = ""

        assert (
            result == "ValueError: Invalid command. Expected: '-c, -l, -w, -m, or None"
        )
