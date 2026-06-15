import sys
import platform
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.align import Align

import pyfiglet

from features.commands import commands
from features.functions import speech_to_text as stt
from versions.versions import JARVISVersions
from features.commands import process_command

from features.commands.errors.__logger import (
    __logs_errors
)

from features.commands.errors.__errors_handler import (
    __errors_handler
)


console = Console()

SESSION_HISTORY = []


def jarvis_banner():

    commands.clear_screen()

    banner = pyfiglet.figlet_format(
        "JARVIS",
        font="slant"
    )

    console.print(
        Panel(
            Align.center(
                f"[cyan]{banner}[/cyan]"
            ),
            title="[green]AI Assistant[/green]",
            subtitle=f"[yellow]{JARVISVersions.get_version()}[/yellow]"
        )
    )


def startup_diagnostics():

    console.print(
        Panel(
            f"""
System Time : {datetime.now()}
Platform    : {platform.system()}
Python      : {platform.python_version()}
Status      : Online
            """,
            title="Diagnostics"
        )
    )


def startup_message():

    console.print(
        Panel(
            "[green]Initialization Complete[/green]\n"
            "All Systems Operational.",
            title="System Status"
        )
    )

    try:
        stt.say(
            "Initialization complete. "
            "All systems operational. "
            "How may I assist you, Sir?"
        )
    except Exception:
        pass


def shutdown():

    try:
        stt.say("Shutting down systems.")
    except Exception:
        pass

    console.print(
        Panel(
            "[red]JARVIS Offline[/red]",
            title="Shutdown"
        )
    )

    sys.exit(0)


def execute_command(command):

    try:

        SESSION_HISTORY.append(command)

        if command.lower() == "history":

            return console.print(
                Panel(
                    "\n".join(SESSION_HISTORY[-20:]),
                    title="Command History"
                )
            )

        if command.lower() == "system info":

            return console.print(
                Panel(
                    f"""
OS      : {platform.system()}
Python  : {platform.python_version()}
Version : {JARVISVersions.get_version()}
                    """,
                    title="System Information"
                )
            )

        result = process_command(command)

        console.print(
            Panel(
                str(result),
                title="Result"
            )
        )

    except Exception as error:

        __logs_errors(error)

        console.print(
            Panel(
                __errors_handler(error),
                title="Error"
            )
        )


def voice_mode():

    try:

        command = stt.user_voice_commands()

        if not command:

            console.print(
                "[yellow]No voice command detected.[/yellow]"
            )

            return

        console.print(
            f"[cyan]Voice >[/cyan] {command}"
        )

        execute_command(command)

    except Exception as error:

        __logs_errors(error)

        console.print(
            Panel(
                __errors_handler(error),
                title="Voice Error"
            )
        )


def keyboard_mode():

    command = input("\nCommand > ").strip()

    if not command:
        return

    if command.lower() in (
        "exit",
        "quit",
        "shutdown"
    ):
        shutdown()

    execute_command(command)


def main():

    try:

        jarvis_banner()

        startup_diagnostics()

        startup_message()

        while True:

            try:

                mode = input(
                    "\n[V] Voice | [K] Keyboard > "
                ).strip().lower()

                if mode == "v":

                    voice_mode()

                elif mode == "k":

                    keyboard_mode()

                elif mode in (
                    "exit",
                    "quit",
                    "shutdown"
                ):

                    shutdown()

                else:

                    console.print(
                        "[yellow]Invalid Mode.[/yellow]"
                    )

            except KeyboardInterrupt:

                shutdown()

            except Exception as error:

                __logs_errors(error)

                console.print(
                    Panel(
                        __errors_handler(error),
                        title="Runtime Error"
                    )
                )

    except Exception as error:

        __logs_errors(error)

        console.print(
            Panel(
                __errors_handler(error),
                title="Startup Error"
            )
        )


if __name__ == "__main__":
    main()