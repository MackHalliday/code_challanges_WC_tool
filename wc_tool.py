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
        elif num_arg == 2:
            self.arg_option = split_command[0]
            self.file_name = split_command[1]
        else:
            raise ValueError(
                "Invalid command format. Expected: 'file_name.txt' or '-option file_name.text'"
            )

    def run_command(self):
        self.parse_command()

        value = {
            "-c": self.byte_size,
            "-l": self.count_lines,
            "-w": self.count_words,
            "-m": self.count_characters,
        }

        if self.arg_option is None:
            value_to_str = f"{value['-l']()}  {value['-w']()}  {value['-c']()}"
        elif self.arg_option in value.keys():
            value_to_str = f"{value[self.arg_option]()}"
        else:
            raise ValueError(
                "Invalid command. Expected: '-c, -l, -w, -m, or None"
            )

        return f"{value_to_str} {self.file_name}"

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
