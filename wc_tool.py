import os


class WCTool():
    def __init__(self, command):
        self.command = command

    def run_command(self):
        arg_option, file_name = self.parse_command()
        if arg_option == "-c":
            return os.path.getsize(file_name)

    def parse_command(self):
        return self.command.split()
