#3

text = input("Введите текст: ")
count = 0

for i in text:
    if i in ['.', '!', '?']:
        count += 1

print("Кол-во предложений в тексте:", count)