current_status = "В процессе" #Текущий статус заметки

print(f"Текущий статус заметки: {current_status}") # Выведение на экран текущего статуса заметки

new_status = input("""Выберите новый статус заметки: 
1. Завершено 
2. В процессе
3. Отложено
Для ввода используйте значение от 1 до 3 или введите значение в текстовом формате
""") # Запрос ввода нового статуса заметки

while new_status not in ["1", "2", "3", "Завершено", "В процессе", "Отложено"]: # Запуск цикла правильности ввода, пока пользователь не выберет значение с 1-3, будет необходимо осуществлять ввод заново
    print("Введено неправильное значение! Пожалуйста введите число от 1 до 3!")
    new_status = input("""Выберите новый статус заметки: 
    1. Выполнено 
    2. В процессе
    3. Отложенно
    """)

status_option = {'1': "Выполнено", '2': "В процессе", '3': "Отложенно", 'Завершено': "Завершено", 'В процессе': "В процессе", 'Отложено': "Отложено"} # Словарь, в котором ключи соотвествуют необходимому значению

current_status = status_option[new_status] # Обновляется текущий статус заметки

print(f"Статус заметки обновлен: {current_status}") # Вывод на экран нового статуса заметки