from main import main


def auto_run():
    main()

if __name__ == " __main__ ":
    while True:
       try:
           auto_run()
           if auto_run:
               print(RuntimeError)

           if auto_run:
               print("[Error:] Invaid Command! please try again.")
               auto_run()
               
       except Exception as e:
            raise e