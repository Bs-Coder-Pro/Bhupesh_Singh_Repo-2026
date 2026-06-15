from main.features.commands import clear_screen

clear_screen()


def jarvis_anger():
    with open("/main/features/emotions/anger/anger.txt", "w") as auto_write:
        auto_writer = auto_write.write()
        print(auto_writer)

    clear_screen()


jarvis_anger()


def anger_runner():
    while True:
        try:
            jarvis_anger()

        except ModuleNotFoundError as mnfe:
            raise mnfe

        except NameError as ne:
            raise ne

        except Exception as e:
            clear_screen()
            raise e
