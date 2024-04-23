"""
Дорабатываем функции из предыдущих задач. 
Генерируйте файлы в указанную директорию — отдельный параметр функции. 
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os
import random
import string

def generate_files_with_extensions(directory, extensions_count, files_per_extension):
    extensions = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in range(extensions_count)]
    for extension in extensions:
        create_files_with_extension(directory, extension, num_files=files_per_extension)

def create_files_with_extension(directory, extension, num_files, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for _ in range(num_files):
        file_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(min_length, max_length)))
        full_file_name = os.path.join(directory, file_name + '.' + extension)
        if not os.path.exists(full_file_name):
            file_size = random.randint(min_bytes, max_bytes)
            create_file(full_file_name, file_size)

def create_file(file_name, file_size):
    with open(file_name, 'wb') as f:
        f.write(bytearray(random.getrandbits(8) for _ in range(file_size)))

# Пример использования функции
generate_files_with_extensions("/Users/pelmeshka/Documents/Обучение/Python погружение/lessons", 5, 10)
