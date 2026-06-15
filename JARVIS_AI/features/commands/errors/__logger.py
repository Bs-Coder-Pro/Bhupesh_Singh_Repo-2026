# features/commands/errors/__logger.py

from datetime import datetime


def __logs_errors(error):

    try:

        with open(
            "error_logs.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"[{datetime.now()}] "
                f"{type(error).__name__}: "
                f"{error}\n"
            )

    except Exception:
        pass