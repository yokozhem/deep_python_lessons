"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import csv
import json

def save_to_csv():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл с данными не найден.")
        return

    try:
        with open('user_data.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Access Level', 'User ID', 'Name'])
            for level, users in data.items():
                for user_id, user_info in users.items():
                    writer.writerow([level, user_id, user_info['name']])
        print("Данные успешно сохранены в файле user_data.csv")
    except Exception as e:
        print(f"Произошла ошибка при сохранении данных в файл CSV: {e}")

if __name__ == "__main__":
    save_to_csv()
