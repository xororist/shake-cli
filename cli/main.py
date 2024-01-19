import os
import click
import importlib

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "commands")
        )
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                command_name = filename.replace("cmd_", "").replace(".py", "")
                commands.append(command_name)
        commands.sort()
        print("List of commands:", commands)  # Add this line for debugging
        return commands

    def get_command(self, ctx, name):
        try:
            module_path = f"cli.commands.cmd_{name}"
            mod = importlib.import_module(module_path)
        except ImportError:
            return
        return getattr(mod, name, None)

@click.command(cls=ComplexCLI)
def cli():
    """Welcome to Shake! An all-in-one cli utility tool!"""
    pass


