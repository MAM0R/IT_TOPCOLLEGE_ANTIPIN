#3 День недели

week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
while True:
    try:
        need_day = int(input("Введите номер дня недели: "))
        if need_day < 1 or need_day > 7:
            raise IndexError
        else:
            if need_day == 1:
                print(week_days[0])
            if need_day == 2:
                print(week_days[1])
            if need_day == 3:
                print(week_days[2])
            if need_day == 4:
                print(week_days[3])
            if need_day == 5:
                print(week_days[4])
            if need_day == 6:
                print(week_days[5])
            if need_day == 7:
                print(week_days[6])
        
    except IndexError:
        print("Нет такого дня")
        break
    except ValueError:
        print("Введите номер дня")
        break
    finally:
        print("Проверка завершена")