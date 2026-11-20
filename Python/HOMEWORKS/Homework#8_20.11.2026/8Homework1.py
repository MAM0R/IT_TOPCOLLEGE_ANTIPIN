#1 Число или текст?

while True:
    try:
        num = int(input("Введите целое число: "))
        ans = num ** 2

        print("Квадрат этого числа:", ans)
        break

    except ValueError:
        print("Введите целое число!")

