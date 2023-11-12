import os


class WCTool:
    def __init__(self, file_path, optional_args):
        self.file_path = file_path
        self.optional_args = optional_args

    def run_command(self):
        value = {
            "-c": self.byte_size,
            "-l": self.count_lines,
            "-w": self.count_words,
            "-m": self.count_characters,
        }

        value_to_str = ""
        
        for arg in self.optional_args:
            value_to_str += f"{value[arg]()} "

        # if self.optional_args is None:
        #     value_to_str = f"{value['-l']()}  {value['-w']()}  {value['-c']()}"
        # elif self.optional_args in value.keys():
        #     value_to_str = f"{value[self.optional_args]()}"
        # else:
        #     raise ValueError("Invalid command. Expected: '-c, -l, -w, -m, or None")

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
