"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Дополните id до 10 цифр незначащими нулями. 
В именах первую букву сделайте прописной. 
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.

"""
import csv
import json

def read_modify_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Пропускаем заголовок
            data = []
            for row in reader:
                access_level, user_id, name = row
                # Дополнение ID до 10 цифр незначащими нулями
                padded_user_id = user_id.zfill(10)
                # Преобразование первой буквы имени в прописную
                formatted_name = name.capitalize()
                # Генерация хеша на основе имени и идентификатора
                hash_value = hash(name + user_id)
                # Создание словаря с обновленными данными
                updated_row = {
                    "Access Level": access_level,
                    "User ID": padded_user_id,
                    "Name": formatted_name,
                    "Hash": hash_value
                }
                data.append(updated_row)
    except FileNotFoundError:
        print("Файл с данными не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении данных из файла CSV: {e}")
        return

    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Данные успешно сохранены в файле {output_file}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении данных в файл JSON: {e}")

if __name__ == "__main__":
    read_modify_csv("user_data.csv", "updated_user_data.json")
