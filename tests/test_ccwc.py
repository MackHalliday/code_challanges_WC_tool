class TestWCTool:
    def test_can_return_number_of_bytes_in_file(self):
        command = "python3 ccwc/ccwc.py -c tests/test.txt"
        result = ""

        assert result == "342190 test.txt"

    def test_can_return_number_of_lines_in_file(self):
        pass
        command = "-l test.txt"
        result = ""

        assert result == "7145 test.txt"

    def test_can_return_number_of_words_in_file(self):
        pass
        command = "-w test.txt"
        result = ""

        assert result == "58164 test.txt"

    def test_can_return_number_of_characters_in_file(self):
        pass
        command = "-m test.txt"
        result = ""

        assert num_of_characters == "339292 test.txt"

    def test_can_return_bytes_line_word_as_default_option(self):
        pass
        command = "test.txt"
        result = ""

        assert result == "7145  58164  342190 test.txt"

    def test_error_handling_for_invalid_input(self):
        pass
        command = "-z test.txt"
        result = ""

        assert (
            result == "ValueError: Invalid command. Expected: '-c, -l, -w, -m, or None"
        )
