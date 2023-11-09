from wc_tool import WCTool


class TestWCTool:
    def test_can_return_number_of_bytes_in_file(self):
        command = "-c test.txt"
        num_of_bytes = WCTool(command).run_command()

        assert num_of_bytes == "342190 test.txt"

    def test_can_return_number_of_lines_in_file(self):
        command = "-l test.txt"
        num_of_lines = WCTool(command).run_command()

        assert num_of_lines == "7145 test.txt"

    def test_can_return_number_of_words_in_file(self):
        command = "-w test.txt"
        num_of_words = WCTool(command).run_command()

        assert num_of_words == "58164 test.txt"
