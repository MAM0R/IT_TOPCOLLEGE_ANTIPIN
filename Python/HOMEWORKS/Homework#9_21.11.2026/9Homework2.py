#2

text = input("Введите текст: ")
reserved_words = input("Введите зарезервированные слова через пробел: ").lower().split()

text_words = text.split()
result = []

for i in text_words:
    if i.lower() in reserved_words:
        result.append(i.upper())
    else:
        result.append(i)

print(" ".join(result))
