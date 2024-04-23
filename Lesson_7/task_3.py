"""
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
При достижении конца более короткого файла, возвращайтесь в его начало.

"""

def process_files(numbers_file, names_file, result_file):
    with open(numbers_file) as num_file, open(names_file) as name_file, open(result_file, "w") as res_file:
        while True:
            number_line = num_file.readline().strip()
            name_line = name_file.readline().strip()

            if not number_line or not name_line:
                break  # если достигнут конец одного из файлов, прекращаем чтение

            number_parts = number_line.split("|")
            name = name_line.strip()

            num1 = int(number_parts[0])
            num2 = float(number_parts[1])

            result = num1 * num2
            if result < 0:
                result = abs(result)
                name = name.lower()
            else:
                result = round(result)

            res_file.write(f"{name}: {result}\n")

process_files("numbers.txt", "pseudo_names.txt", "results.txt")
