from finaltask.app import App


def main():
    app = App()
    try:
        app.start()
    except Exception as e:
        print(e)
    print(app.data)


if __name__ == '__main__':
    main()