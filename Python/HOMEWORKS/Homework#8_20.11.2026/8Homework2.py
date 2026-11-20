#2 Безопасное деление

try:
    num1 = int(input("Введите 1-ое число: "))
    num2 = int(input("Введите 2-ое число: "))
    ans = num1 / num2

    print("Ответ:", ans)

except ValueError:
    print("Нужно ввести два целых числа")

except ZeroDivisionError:
    print("На ноль делить нельзя")

