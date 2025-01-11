user_name, content, status, created_date, issue_date = input("Введите имя пользователя: "), input("Введите описание заметки: "), input("Введите статус выполнения: "), input('Введите дату начала выполнения в формате "01-Feb-2025": '), input('Введите сроки выполнения в формате "01-Feb-2025": ')
title1 = input("Введите название заголовка №1: ")
title2 = input("Введите название заголовка №2: ")
title3 = input("Введите название заголовка №3: ")
title_list = [title1, title2, title3]
note = [user_name, content, status, created_date[0:6], issue_date[0:6], title_list]
print(note)