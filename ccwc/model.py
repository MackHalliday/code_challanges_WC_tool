import os


class CCWCModel:
    def __init__(self, file_path, optional_args):
        self.file_path = file_path
        self.optional_args = optional_args

    def run_command(self):
        value_to_str = ""

        # TODO is there a better way to determine if args are used
        if self.optional_args.bytes:
            value_to_str = self.byte_size()

        elif self.optional_args.lines:
            value_to_str = self.count_lines()

        elif self.optional_args.words:
            value_to_str = self.count_words()

        elif self.optional_args.characters:
            value_to_str = self.count_characters()

        else:
            return f"{self.byte_size()} {self.count_words()}  {self.count_characters()}"

        return f"{value_to_str} {self.file_path}"

    def byte_size(self):
        return os.path.getsize(self.file_path)

    def count_lines(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total_lines = len(lines)
        return total_lines

    def count_words(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            total_words = len(words)

        return total_words

    def count_characters(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()
            total_characters = len(content)

        total_lines = self.count_lines()
        total_characters += total_lines

        return total_characters
