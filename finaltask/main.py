import os
import traceback


from finaltask.app import App, IOException


def main():
    app = App()
    input_mode = True
    while input_mode:
        try:
            input_mode = app.start()
        except IOException:
            traceback.print_exc()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()