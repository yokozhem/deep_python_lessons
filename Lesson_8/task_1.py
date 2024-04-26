"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.
"""

import json

def convert_to_json(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = f.readlines()
        
        json_data = {}
        for line in data:
            name, product = line.strip().split(': ')
            json_data[name.capitalize()] = float(product)
        
        with open(output_file, 'w') as f:
            json.dump(json_data, f, indent=4)
        
        print(f"Data from '{input_file}' successfully converted to JSON format and saved to '{output_file}'.")
    
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Пример использования:
convert_to_json("results.txt", "output.json")
