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

        value = {
            "-c": self.byte_size,
            "-l": self.count_lines,
            "-w": self.count_words,
            "-m": self.count_characters,
        }

        if self.arg_option is None:
            value = self.no_option_values()
            return f"{value[0]}  {value[1]}  {value[2]} {self.file_name}"

        return f"{value.get(self.arg_option)()} {self.file_name}"

    def no_option_values(self):
        return self.count_lines(), self.count_words(), self.byte_size()

    def byte_size(self):
        return os.path.getsize(self.file_name)

    def count_lines(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total_lines = len(lines)
        return total_lines

    def count_words(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            total_words = len(words)

        return total_words

    def count_characters(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            content = file.read()
            total_characters = len(content)

        total_lines = self.count_lines()
        total_characters += total_lines

        return total_characters
