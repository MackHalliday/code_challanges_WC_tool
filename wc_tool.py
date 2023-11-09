import os


class WCTool:
    def __init__(self, command):
        self.command = command
        self.arg_option = None
        self.file_name = None

    def parse_command(self):
        arg_option, file_name = self.command.split()
        self.arg_option = arg_option
        self.file_name = file_name

    def run_command(self):
        self.parse_command()

        if self.arg_option == "-c":
            option_value = os.path.getsize(self.file_name)

        if self.arg_option == "-l":
            option_value = self.count_lines(self.file_name)

        return f"{option_value} {self.file_name}"

    def count_lines(self, file_name):
        with open(self.file_name) as file:
            lines = file.readlines()
            total_lines = len(lines)
        return total_lines
