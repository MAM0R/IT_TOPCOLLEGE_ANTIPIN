#1

line_input = input("Введите строку: ")
line_input = line_input.lower()
line_input = line_input.replace(" ", "")
line_input = line_input.replace(".", "")
line_input = line_input.replace(",", "")

line_reversed = line_input[::-1]

if line_input == line_reversed:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")