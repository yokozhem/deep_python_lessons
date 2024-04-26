"""
Доработаем предыдущую задачу. 
Создайте новую функцию которая генерирует файлы с разными расширениями. 
Расширения и количество файлов функция принимает в качестве параметров. 
Количество переданных расширений может быть любым. 
Количество файлов для каждого расширения различно. 
Внутри используйте вызов функции из прошлой задачи.
"""
import random
import string

def generate_files_with_extensions(extensions_count, files_per_extension):
    extensions = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in range(extensions_count)]
    for extension in extensions:
        create_files_with_extension(extension, num_files=files_per_extension)

def create_files_with_extension(extension, num_files, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    for _ in range(num_files):
        file_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(min_length, max_length)))
        file_size = random.randint(min_bytes, max_bytes)
        create_file(file_name + '.' + extension, file_size)

def create_file(file_name, file_size):
    with open(file_name, 'wb') as f:
        f.write(bytearray(random.getrandbits(8) for _ in range(file_size)))

# Пример использования функции
generate_files_with_extensions(5, 10)
