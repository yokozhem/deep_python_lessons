"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла. 
"""

import pickle
import csv

def convert_pickle_to_csv(pickle_file, csv_file):
    try:
        # Чтение содержимого из pickle файла
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)

        # Проверка на пустой список данных
        if not data:
            print("Список словарей пуст.")
            return

        # Получение заголовков столбцов из ключей первого словаря
        fieldnames = list(data[0].keys())

        # Запись данных в CSV файл
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Данные из {pickle_file} успешно преобразованы в CSV файл {csv_file}")
    except FileNotFoundError:
        print(f"Файл {pickle_file} не найден.")
    except EOFError:
        print(f"Файл {pickle_file} пуст или его структура не соответствует ожидаемой.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    pickle_file_path = "/Users/pelmeshka/Documents/Обучение/Python погружение/lessons/updated_user_data.pickle"
    csv_file_path = "data.csv"
    convert_pickle_to_csv(pickle_file_path, csv_file_path)
