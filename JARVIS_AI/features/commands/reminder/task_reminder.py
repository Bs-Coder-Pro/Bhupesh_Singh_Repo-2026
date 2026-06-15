from features import fileManager


def task_reminder():
    try:
        manage_files = fileManager()
        return manage_files

    except FileNotFoundError as file_not_found_error:
        raise file_not_found_error

    except NameError:
        return "Reminder Code: [Pending...]"


def tasks():
    return "Task Code: [Pending...]"


def default_tasks():
    return {
        "alarm": "Set Alarm Code: [Pending...]",
        "daily_tasks": "Default Task Code: [Pending...]"
    }


def final_reminder():
    try:
        print(tasks())

        reminder = task_reminder()
        if reminder:
            print(reminder)

        defaults = default_tasks()
        print(defaults["alarm"])
        print(defaults["daily_tasks"])

    except ModuleNotFoundError as module_not_found_error:
        raise module_not_found_error

    except RuntimeError as run_time_error:
        raise run_time_error


final_reminder()