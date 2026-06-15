# features/commands.py

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def process_command(command: str):
    """
    Main command processor
    """

    command = command.strip()

    return f"Executing: {command}"