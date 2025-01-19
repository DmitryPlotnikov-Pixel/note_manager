from datetime import datetime # Импортируем модуль из библиотеки, это поможет нам для работы с датами

datetime_now = datetime.now() # Текущая дата

formatted_datetime = datetime_now.strftime("%d.%m.%Y") # Преобразовываем дату в нужный нам формат, исключая время

datetime_now = datetime.strptime(formatted_datetime, "%d.%m.%Y") # Преобразовываем строку в объект datetime,

print(f"Текущая дата: {formatted_datetime}") # Выводит текущу дату на консоль

while True: # Начало цикла, будет продолжаться, пока ПЗ не введет корректную дату, в случае ошибки, повторяется
    try: # Запускаем блок проверки ошибок
        issue_date = input("Введите срок выполнения (в формате дд.мм.гггг, например 25.12.2024): " ) # Просит пользователя ввести срок выполнения в нужном формате

        issue_date_ = datetime.strptime(issue_date,"%d.%m.%Y") # Преобразует дату(строку) в объект datetime

        time_difference = issue_date_ - datetime_now # Вычесляет раницу между сроком выполнения и текущей датой
        days_difference = time_difference.days # Разница в сроках выполнения в днях

        if days_difference > 0: # Проверка разницы и вывод в соотвествующего значения
            print(f"До окончания выполнения осталось {days_difference} дней!")
        elif days_difference < 0:
            print(f"Срок выполнения истек {abs(days_difference)} дней назад!")
        else:
            print("Необходимо закончить сегодня!")

        break # Выходим из цикла при выполнение условий

    except ValueError: # Если пользователь ввел неправильный формат даты
        print("Неправильный формат даты! Пожалуйста, введите дату в правильном формате, например 25.12.2024!")