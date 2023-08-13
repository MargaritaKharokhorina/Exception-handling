# Дан следующий код, исправьте его там, где требуется:
# public static void main(String[] args) throws Exception {
#    try {
#        int a = 90;
#        int b = 3;
#        System.out.println(a / b);
#        printSum(23, 234);
#        int[] abc = { 1, 2 };
#        abc[3] = 9;
#    } catch (Throwable ex) {
#        System.out.println("Что-то пошло не так...");
#    } catch (NullPointerException ex) {
#        System.out.println("Указатель не может указывать на null!");
#    } catch (IndexOutOfBoundsException ex) {
#        System.out.println("Массив выходит за пределы своего размера!");
#    }
# }
# public static void printSum(Integer a, Integer b) throws FileNotFoundException {
#    System.out.println(a + b);
# }

# В printSum ни к чему исключение FileNotFoundException, кроме того, и сама функция бесполезная (просто складывает 2 целых числа)

# int[] abc = {1, 2} --> объявлено 2 элемента
# abc[3] = 9 --> вызывается 3-й по индексу; значит, элементов должно быть 4

# catch (Throwable ex) общее исключение должно кидаться после всех остальных исключений


def printSum(a: int, b: int):
    print(a + b)


def main():
    try:
        a: int = 90
        b: int = 3
        print(a / b)
        # printSum(23, 234)
        print(23 + 234)
        # abc: list[int] = [1, 2]
        abc: list[int] = [1, 2, 3, 4]
        abc[3] = 9
    except IndexError:
        print("Массив выходит за пределы своего размера!")
    except Exception:
        print("Что-то пошло не так...")


if __name__ == "__main__":
    main()

