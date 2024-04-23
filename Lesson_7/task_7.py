"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
Каждая группа включает файлы с несколькими расширениями. 
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
import shutil

def sort_files(source_dir, destination_dirs):
    # Проверяем, существует ли исходная директория
    if not os.path.exists(source_dir):
        print(f"Директория {source_dir} не существует.")
        return
    
    # Создаем директории назначения, если они не существуют
    for dir_name in destination_dirs.values():
        os.makedirs(dir_name, exist_ok=True)
    
    # Получаем список файлов в исходной директории
    files = os.listdir(source_dir)
    
    # Сортируем файлы
    for file in files:
        # Получаем полный путь к файлу
        file_path = os.path.join(source_dir, file)
        # Проверяем, является ли файл обычным файлом
        if os.path.isfile(file_path):
            # Получаем расширение файла
            _, extension = os.path.splitext(file)
            # Ищем директорию назначения для данного расширения
            destination_dir = destination_dirs.get(extension.lower(), None)
            # Если директория назначения найдена, перемещаем файл туда
            if destination_dir:
                shutil.move(file_path, destination_dir)
                print(f"Файл {file} перемещен в {destination_dir}")
            else:
                print(f"Файл {file} не подходит для сортировки")
        else:
            print(f"{file} не является обычным файлом и будет проигнорирован")

# Пример использования
source_directory = "/path/to/source_directory"
destination_directories = {
    ".mp4": "/path/to/video_directory",
    ".jpg": "/path/to/image_directory",
    ".txt": "/path/to/text_directory"
}

sort_files(source_directory, destination_directories)
