import main
import pathlib as plib
from features.commands import commands as cmd
from features.functions.auto import auto
from main import main


def __exists() -> FileExistsError:
    document_existence = f"document: [file and folder existence]..[pending]"
    path = plib.__path__(__file__)
    return (path, document_existence)


def file_organizer() -> FileNotFoundError:
    f_organizer = "file organizer..[pending]"
    return f_organizer


def folder_organizer() -> NameError:
    dir_organizer = "directory organizer..[pending]"
    return dir_organizer


def add_file_extention() -> IndexError:
    add_extention = "add_extention..[pending]"
    return add_extention


def file_remover():
    remover = "add_extention..[pending]"
    return remover


def documents_finder(self, file, file_location, folder, extention):
    find = [f"""
            {self.file} {file},
            {self.folder} {folder},
            {self.extention} {extention}
            {self.file_location} {file_location}
            """]

    return (find, __exists(__path__))


def data_restore():
    restore = "add_extention..[pending]"
    return restore


def file_renamer():
    renamer = "file renamer..[pending]"
    return renamer


def directory_renamer():
    dir_renamer = "file renamer..[pending]"
    return dir_renamer


def multi_file_renamer():
    add_extention = "add_extention..[pending]"
    return add_extention


def multi_directories_renamer():
    add_extention = "add_extention..[pending]"
    return add_extention


def organizer_runner() -> main:

    try:
        __exists()
        data_restore()
        file_renamer()
        file_remover()
        file_organizer()
        folder_organizer()
        documents_finder()
        directory_renamer()
        add_file_extention()
        multi_file_renamer()
        multi_directories_renamer()

    except (
        FileNotFoundError,
        ModuleNotFoundError,
        NameError,
        TypeError,
        EOFError,
        ValueError,
        ImportError,
        MemoryError,
        OverflowError,
        LookupError,
        SystemError,
        RuntimeError,
        TimeoutError,
        WindowsError,
        AttributeError,
        RecursionError,
        InterruptedError,
        ConnectionError,
        ConnectionRefusedError,
        ConnectionAbortedError,
        ConnectionResetError,
        FileExistsError,
        PermissionError,
        EnvironmentError,
        IndentationError,
        NotADirectoryError,
        UnboundLocalError,
        ChildProcessError,
        IsADirectoryError,
        UnicodeTranslateError,
        PythonFinalizationError,
    ) as errors:
        raise errors


organizer_runner()
