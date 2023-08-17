from datetime import datetime, date

class Personality:
    def __init__(self, last_name: str, first_name: str, middle_name: str, birthdate: str,
                 telephone: str, gender: str):
        self.__full_name_is_alpha(first_name, middle_name, last_name)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

        self.__is_date(birthdate)
        self.birthdate = birthdate

        self.__is_telephone(telephone)
        self.telephone = telephone
        if not isinstance(gender, str) or not (len(gender) == 1 and gender in ('m', 'f')):
            raise ValueError("Гендер не является символом m ли f")
        self.gender = gender

    @staticmethod
    def __is_date(date_value: str):
        date_list = date_value.split(".")
        if len(date_value) < 10 or len(date_list) != 3:
            raise ValueError("Дата не соответствует формату dd.mm.yyyy")
        for i in date_list:
            try:
                el = int(i)
            except ValueError:
                raise ValueError("Элемент в дате рождения не является целым числом")
        if 31 < int(date_list[0]):
            raise ValueError("Число дня больше 31")
        elif int(date_list[0]) < 1:
            raise ValueError("Число дня меньше 1")
        if 12 < int(date_list[1]):
            raise ValueError("Число месяца больше 12")
        elif int(date_list[1]) < 1:
            raise ValueError("Число месяца меньше 1")
        if datetime.strptime(date_value, '%d.%m.%Y').date() > date.today():
            raise ValueError("Дата рождения больше даты сегодняшнего дня")

    @staticmethod
    def __full_name_is_alpha(first_name: str, middle_name: str, last_name: str):
        if not first_name.isalpha():
            raise ValueError("Имя должно состоять только из букв")
        if not middle_name.isalpha():
            raise ValueError("Отчество должно состоять только из букв")
        if not last_name.isalpha():
            raise ValueError("Фамилия должно состоять только из букв")

    @staticmethod
    def __is_telephone(telephone: str):
        if not telephone.isdigit():
            raise ValueError("Номер телефона не является целым беззнаковым числом")
        if len(telephone) < 6:
            raise ValueError("Номер телефона должен содержать от 6 цифр")
        if len(telephone) > 11:
            raise ValueError("Номер телефона не должен превышать 11 цифр")

    def __str__(self):
        return " ".join((self.last_name, self.first_name, self.middle_name, self.birthdate, self.telephone, self.gender))