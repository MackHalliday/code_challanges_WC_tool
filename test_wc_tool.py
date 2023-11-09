from wc_tool import WCTool


class TestWCTool:
    def test_can_return_number_of_bytes_file(self):
        command = "-c test.txt"
        num_of_bytes = WCTool(command).run_command()

        assert num_of_bytes == 342190
