
#возвести число в квадрат
def square(x):
    y = x ** 2
    return y
result = square(10)
print(result)


#возвести в определённую степень число
def exponent(x, s):
    return x ** s
res_exp = exponent(10, 5)
print(res_exp)


#среднее арифметическое
def average(*args): # * кортеж, появляется возможность принимать любое количество позиционных аргументов (от нуля до бесконечности)
    return sum(args) / len(args)
res_avg = average(321, 12312, 1231245, 412513, 4213412)
print(res_avg)


#приветствие для имени Анна
def greet(name):
    print("Hello", name)
greet("Anna")


#приветствие для разных имён
import random
greetings = ["hi", "hello", "ni hao", "bonjour", "привет"]

def greet_anyone():
    name = input("Введите имя: ")
    random_greet = random.choice(greetings) #выбрать рандомное значение из списка
    print(random_greet, name)
greet_anyone()


names = []
def user_input():
    global city
    city = "Irkutsk"
    print(city)
    name = input("Enter your name: ")
    second_name = input("Enter your second name: ")
    names.append(f"{name} {second_name}")
    greet(name)

while True:
    user_input()
    print(names)
    print(city)
    break