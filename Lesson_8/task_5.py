"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import os
import json
import pickle

def convert_json_to_pickle(directory):
    try:
        # Проверяем, существует ли указанная директория
        if not os.path.exists(directory):
            print("Указанная директория не существует.")
            return

        # Проходим по всем файлам в указанной директории
        for filename in os.listdir(directory):
            if filename.endswith(".json"):  # Проверяем, что файл имеет расширение .json
                json_file = os.path.join(directory, filename)
                pickle_file = os.path.splitext(json_file)[0] + ".pickle"  # Создаем имя для pickle файла

                # Чтение содержимого JSON файла
                with open(json_file, "r") as f:
                    json_data = json.load(f)

                # Сохранение содержимого в pickle файл
                with open(pickle_file, "wb") as f:
                    pickle.dump(json_data, f)

                print(f"Файл {json_file} успешно преобразован в {pickle_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    directory_path = "/Users/pelmeshka/Documents/Обучение/Python погружение/lessons"
    convert_json_to_pickle(directory_path)
