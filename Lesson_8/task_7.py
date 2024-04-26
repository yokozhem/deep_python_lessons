"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку.
"""

import csv
import pickle

def read_csv_to_pickle_string(csv_file):
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = [row for row in reader]
            pickle_string = pickle.dumps(data)
            return pickle_string
    except FileNotFoundError:
        print(f"Файл {csv_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    csv_file_path = "data.csv"
    pickle_string = read_csv_to_pickle_string(csv_file_path)
    print(pickle_string)
