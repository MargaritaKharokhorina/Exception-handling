from finaltask.data import Data
from finaltask.personal_inf import Personality


class IOException(IOError):
    def __init__(self, path: str = None, msg: str = "Файл не найден"):
        if path:
            super().__init__(f"{msg}: '{path}'")
        else:
            super().__init__(f"{msg}")



class App:
    def __init__(self):
        self.__data = Data(list[Personality]())
        self.__code_errors = {1: "Количество введенных данных меньше требуемого",
                              2: "Количество введенных данных больше требуемого",
                              }

    def __input(self):
        data = self.__input_data()
        if data == 1 or data == 2:
            print(self.__code_errors[data])
            return
        profile = Personality(*data)
        self.__data.append(profile)
        self.__create_file(profile.last_name, str(profile))

    @staticmethod
    def __input_data():
        data = input().split(" ")
        if len(data) < 6:
            return 1
        elif len(data) > 6:
            return 2
        return data

    @property
    def data(self):
        return self.__data

    def start(self):
        self.__input()

    def __create_file(self, filename: str, text: str):
        if self.__file_exists(filename):
            filename = self.__find_free_filename(filename)
        try:
            with open(filename, encoding='utf-8', mode="w") as file:
                file.write(text)
        except IOError as e:
            raise IOException(e.filename)

    @staticmethod
    def __file_exists(filename: str):
        try:
            open(filename, mode="r")
        except IOError:
            return False
        return True

    def __find_free_filename(self, filename: str, counter: int = 0):
        if self.__file_exists(filename + "_" + str(counter)):
            return self.__find_free_filename(filename, counter + 1)
        return filename + "_" + str(counter)