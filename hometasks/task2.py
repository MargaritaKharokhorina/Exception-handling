# Если необходимо, исправьте данный код:
# try {
#    int d = 0;
#    double catchedRes1 = intArray[8] / d;
#    System.out.println("catchedRes1 = " + catchedRes1);
# } catch (ArithmeticException e) {
#    System.out.println("Catching exception: " + e);
# }

# массив intArray[8] должен быть объявлен и содержать в себе 9 элементов,
# 8-й по индексу элемент должен быть правильного типа (целое или дробное число)

# если d != 0 и не появится ошибка деления на 0, нужно также перевести catchedRes1 в выводе сообщения в строку
def main():
    intArray: list[int] = [i for i in range(9)]
    try:
        # d: int = 1
        d: int = 0
        catchedRes1: float = intArray[8] / d
        print("catchedRes1 = " + str(catchedRes1))
    except ArithmeticError as e:
        print("Catching exception: " + str(e))


if __name__ == "__main__":
    main()
