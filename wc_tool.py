import os


class WCTool:
    def __init__(self, command):
        self.command = command
        self.arg_option = None
        self.file_name = None

    def parse_command(self):
        split_command = self.command.split()
        num_arg = len(split_command)

        if num_arg == 1:
            self.file_name = split_command[0]
        if num_arg == 2:
            self.arg_option = split_command[0]
            self.file_name = split_command[1]

    def run_command(self):
        self.parse_command()

        if self.arg_option == "-c":
            value = self.file_size()

        if self.arg_option == "-l":
            value = self.count_lines()

        if self.arg_option == "-w":
            value = self.count_words()

        if self.arg_option == "-m":
            value = self.count_characters()

        if self.arg_option is None:
            value = self.no_option_value()
            return f"{value[0]}  {value[1]}  {value[2]} {self.file_name}"

        return f"{value} {self.file_name}"

    def no_option_value(self):
        return self.count_lines(), self.count_words(), self.file_size()

    def file_size(self):
        return os.path.getsize(self.file_name)

    def count_lines(self):
        with open(self.file_name) as file:
            lines = file.readlines()
            total_lines = len(lines)
        return total_lines

    def count_words(self):
        with open(self.file_name) as file:
            content = file.read()
            words = content.split()
            total_words = len(words)

        return total_words

    def count_characters(self):
        with open(self.file_name, "r") as file:
            total_characters = len(file.read())

        return total_characters
