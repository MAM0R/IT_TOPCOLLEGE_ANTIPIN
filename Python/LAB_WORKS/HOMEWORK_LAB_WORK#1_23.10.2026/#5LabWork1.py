#5
"""Пользователь вводит число N. 
Найдите факториал этого числа — произведение всех чисел от 1 до N. 
Обозначается N!."""

N = int(input("Введите N: "))
factorial = 1

for i in range(1, N+1):
    factorial *= i

print(N, "!", " = ", factorial, sep="")