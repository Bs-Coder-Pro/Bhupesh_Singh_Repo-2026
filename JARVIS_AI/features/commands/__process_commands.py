def process_command(command: str):

    try:
        command = command.strip()

        if command.lower().startswith("create folder:"):
            name = command.split(":", 1)[1].strip()
            return f"create_folder{(name)}"

        elif command.lower().startswith("create file:"):
            name = command.split(":", 1)[1].strip()
            return f"create_file{(name)}"

        elif command.lower().startswith("organize:"):
            path = command.split(":", 1)[1].strip()
            return f"organize_folder{(path)}"

        elif command.lower().startswith("delete file:"):
            name = command.split(":", 1)[1].strip()
            return f"delete_file{(name)}"

        elif command.lower().startswith("delete folder:"):
            name = command.split(":", 1)[1].strip()
            return f"delete_folder{(name)}"

        else:
            return f"Unknown command: {command}"

    except IndexError:
        return "Invalid command format."

    except Exception as error:
        return f"Error: {error}"