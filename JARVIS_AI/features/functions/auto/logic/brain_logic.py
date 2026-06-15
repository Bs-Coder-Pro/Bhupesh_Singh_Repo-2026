from features.functions.auto.logic import brain_logic as brain


def memory():
    try:
        with open("features/auth/memory_log.txt", "a+", encoding="utf-8") as memory_logs:
            memory_logs.seek(0)
            return memory_logs.read()
    except FileNotFoundError:
        return ""


def __main_memory():
    try:
        brain()
    except ModuleNotFoundError as module_not_found_error:
        raise module_not_found_error


def brain_runner():
    memory_data = memory()
    print(f"Memory Loaded: {memory_data}")

    __main_memory()


brain_runner()