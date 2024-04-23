"""
Напишите функцию, которая генерирует псевдоимена. 
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. 
Полученные имена сохраните в файл.
"""

import random
import string

def generate_pseudo_names(num_names, file_name):
    vowels = "AEIOU"
    with open(file_name, "w") as file:
        for _ in range(num_names):
            name_length = random.randint(4, 7)
            name = random.choice(vowels).upper()  # начинаем с заглавной гласной буквы
            for _ in range(name_length - 1):
                name += random.choice(string.ascii_letters)  # добавляем остальные буквы
            file.write(name + "\n")

generate_pseudo_names(10, "pseudo_names.txt")
