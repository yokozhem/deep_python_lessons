""" Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке """

""" # Выводим заголовок таблицы
print("Таблица умножения")

# Выводим шапку таблицы
print(" ", end="\t\t")  # Выводим отступ перед таблицей
for i in range(2, 11):
    print(f"{i}              ", end="\t")  # Выводим заголовки столбцов
print()  # Переходим на новую строку

# Выводим тело таблицы
for i in range(2, 11):
    print(i, end="\t\t")  # Выводим заголовок строки с дополнительным отступом
    for j in range(2, 11):
        print(f"{i} * {j} = {i*j}", end="\t")  # Выводим результаты умножения
    print()  # Переходим на новую строку """


for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j} * {i} = {i * j}", end="\t \t")
    print(" ")

print(" ")

for i in range(2, 11):
    for j in range(6, 10):
        print(f"{j} * {i} = {i * j}", end="\t \t")
    print(" ")
