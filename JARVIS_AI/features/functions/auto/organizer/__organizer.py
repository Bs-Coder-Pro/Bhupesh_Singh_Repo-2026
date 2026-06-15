import os
import shutil


def organize_folder(path):
    try:
        extensions = {
            "Images": [".png", ".jpg", ".jpeg", ".gif"],
            "Videos": [".mp4", ".mkv", ".avi"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Archives": [".zip", ".rar"],
        }

        for file in os.listdir(path):
            full_path = os.path.join(path, file)

            if not os.path.isfile(full_path):
                continue

            extension = os.path.splitext(file)[1].lower()

            for folder, exts in extensions.items():
                if extension in exts:
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(full_path, os.path.join(folder_path, file))
                    break

        return "Organization completed."

    except Exception as error:
        return f"Error: {error}"
