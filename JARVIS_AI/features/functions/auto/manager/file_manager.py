import os
import shutil


def create_folder(name):
    try:
        os.makedirs(name, exist_ok=True)
        return f"Folder created: {name}"
    except Exception as error:
        return f"Error: {error}"


def create_file(filename):
    try:
        with open(filename, "w", encoding="utf-8"):
            pass
        return f"File created: {filename}"
    except Exception as error:
        return f"Error: {error}"


def delete_file(filename):
    try:
        os.remove(filename)
        return f"File deleted: {filename}"
    except FileNotFoundError:
        return "File not found."


def delete_folder(folder):
    try:
        shutil.rmtree(folder)
        return f"Folder deleted: {folder}"
    except FileNotFoundError:
        return "Folder not found."


def rename(source, destination):
    try:
        os.rename(source, destination)
        return f"Renamed {source} -> {destination}"
    except Exception as error:
        return f"Error: {error}"


def move(source, destination):
    try:
        shutil.move(source, destination)
        return f"Moved {source} -> {destination}"
    except Exception as error:
        return f"Error: {error}"


def copy(source, destination):
    try:
        shutil.copy2(source, destination)
        return f"Copied {source} -> {destination}"
    except Exception as error:
        return f"Error: {error}"


def list_files(path="."):
    try:
        return os.listdir(path)
    except Exception as error:
        return f"Error: {error}"


def search_file(filename, search_path="."):
    try:
        for root, _, files in os.walk(search_path):
            if filename in files:
                return os.path.join(root, filename)
        return "File not found."
    except Exception as error:
        return f"Error: {error}"