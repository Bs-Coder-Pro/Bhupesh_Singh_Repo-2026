# versions/versions.py

import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


class JARVISVersions:

    VERSION = "v0.0.1"
    CODENAME = "Genesis"
    BUILD = "2026.06.15"
    STATUS = "Development"

    @classmethod
    def get_version(cls):
        return cls.VERSION

    @classmethod
    def get_codename(cls):
        return cls.CODENAME

    @classmethod
    def get_python_version(cls):
        return sys.version

    @classmethod
    def info(cls):

        return {
            "jarvis_version": cls.VERSION,
            "codename": cls.CODENAME,
            "build": cls.BUILD,
            "status": cls.STATUS,
            "python_version": sys.version,
        }

    @classmethod
    def startup_banner(cls):

        console.print(
            Panel(
                f"""
[cyan]JARVIS[/cyan]

Version  : {cls.VERSION}
Codename : {cls.CODENAME}
Build    : {cls.BUILD}
Status   : {cls.STATUS}
Python   : {sys.version.split()[0]}
                """,
                title="[green]Initializing[/green]",
                subtitle="[yellow]System Startup[/yellow]"
            )
        )

    @classmethod
    def display(cls):

        table = Table(
            title="JARVIS Version Information"
        )

        table.add_column(
            "Property",
            justify="left"
        )

        table.add_column(
            "Value",
            justify="left"
        )

        table.add_row(
            "Version",
            cls.VERSION
        )

        table.add_row(
            "Codename",
            cls.CODENAME
        )

        table.add_row(
            "Build",
            cls.BUILD
        )

        table.add_row(
            "Status",
            cls.STATUS
        )

        table.add_row(
            "Python",
            sys.version.split()[0]
        )

        console.print(
            Panel(
                table,
                title="[cyan]JARVIS[/cyan]",
                subtitle="[green]System Information[/green]"
            )
        )


if __name__ == "__main__":

    JARVISVersions.startup_banner()

    JARVISVersions.display()