# features/commands/errors/__errors_handler.py

from features.commands.errors import (
    CommandError,
    VoiceRecognitionError,
    FileManagerError,
    OrganizerError,
    StartupError,
    ShutdownError,
)


def __errors_handler(error) -> str:

    if isinstance(error, CommandError):
        return f"[COMMAND ERROR] {error}"

    elif isinstance(error, VoiceRecognitionError):
        return f"[VOICE ERROR] {error}"

    elif isinstance(error, FileManagerError):
        return f"[FILE MANAGER ERROR] {error}"

    elif isinstance(error, OrganizerError):
        return f"[ORGANIZER ERROR] {error}"

    elif isinstance(error, StartupError):
        return f"[STARTUP ERROR] {error}"

    elif isinstance(error, ShutdownError):
        return f"[SHUTDOWN ERROR] {error}"

    elif isinstance(error, KeyboardInterrupt):
        return "Shutdown Requested By User"

    elif isinstance(error, FileNotFoundError):
        return f"[FILE NOT FOUND] {error}"

    elif isinstance(error, PermissionError):
        return f"[PERMISSION DENIED] {error}"

    elif isinstance(error, ModuleNotFoundError):
        return f"[MODULE NOT FOUND] {error}"

    elif isinstance(error, ImportError):
        return f"[IMPORT ERROR] {error}"

    elif isinstance(error, AttributeError):
        return f"[ATTRIBUTE ERROR] {error}"

    elif isinstance(error, ValueError):
        return f"[VALUE ERROR] {error}"

    elif isinstance(error, TypeError):
        return f"[TYPE ERROR] {error}"

    elif isinstance(error, RuntimeError):
        return f"[RUNTIME ERROR] {error}"

    elif isinstance(error, OSError):
        return f"[OS ERROR] {error}"

    return f"[UNKNOWN ERROR] {type(error).__name__}: {error}"