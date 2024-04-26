"""
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
Первое число int, второе - float разделены вертикальной чертой. 
Минимальное число - -1000, максимальное - +1000. 
Количество строк и имя файла передаются как аргументы функции
"""
import random

def fill_file_with_random_pairs(file_name, num_lines):
    with open(file_name, 'a') as file:
        for _ in range(num_lines):
            int_number = random.randint(-1000, 1000)
            float_number = random.uniform(-1000, 1000)
            file.write(f"{int_number}|{float_number}\n")

fill_file_with_random_pairs("/Users/pelmeshka/Documents/Обучение/Python погружение/доки/тест.txt", 10)
