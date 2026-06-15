# __source_connector.py

from datetime import datetime

from features.commands import __process_commands

from features.commands.errors import (
    __errors_handler,
    __logs_errors
)


class SourceConnector:

    def __init__(self):

        self.start_time = datetime.now()

    def execute(self, command):

        try:

            if not command:
                return "No command received."

            command = str(command).strip()

            if not command:
                return "Empty command."

            result = __process_commands(command)

            return result

        except KeyboardInterrupt:

            return "Operation cancelled by user."

        except Exception as error:

            __logs_errors(error)

            return __errors_handler(error)


connector = SourceConnector()


def create_command(command):

    return connector.execute(command)


def all_connections():

    return connector