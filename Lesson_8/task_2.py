"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
После каждого ввода добавляйте новую информацию в JSON файл. 
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. 
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json

def add_user_info():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'level_1': {}, 'level_2': {}, 'level_3': {}, 'level_4': {}, 'level_5': {}, 'level_6': {}, 'level_7': {}}

    while True:
        name = input("Введите имя пользователя (для завершения введите 'exit'): ")
        if name == 'exit':
            break

        user_id = input("Введите личный идентификатор пользователя: ")
        access_level = int(input("Введите уровень доступа пользователя (от 1 до 7): "))
        if access_level < 1 or access_level > 7:
            print("Уровень доступа должен быть от 1 до 7. Повторите ввод.")
            continue

        data[f"level_{access_level}"][user_id] = {'name': name}

        try:
            with open('user_data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Данные успешно добавлены в файл.")
        except Exception as e:
            print(f"Произошла ошибка при записи данных в файл: {e}")

if __name__ == "__main__":
    add_user_info()
