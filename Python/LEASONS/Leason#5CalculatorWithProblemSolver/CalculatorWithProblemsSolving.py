#Калькулятор с обработкой ошибок

while True:
    try:
        num1 = int(input("Введите 1-ое число: "))
        num2 = int(input("Введите 2-ое число: "))

        operation  = input("Введите операцию (+, -, *, /) ИЛИ exit для выхода из программы: ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "secret":
            raise Exception("Секретное сообщение, вау") #Exception передаёт в текст ошибки текст который написан в ()
        elif operation == "exit":
            break
        else:
            result = "Неизвестный оператор"

        print("Результат:", result)

    except ValueError:
        print("ОШИБКА: Ввод должен быть числом")
    except ZeroDivisionError:
        print("ОШИБКА: Деление на 0 запрещено")
    except Exception:
        print("ОШИБКА")
    else:
        print("Нет ошибок")

    finally: #выполняется всегда
        print("Программа работает, а с ошибками или нет смотреть выше")