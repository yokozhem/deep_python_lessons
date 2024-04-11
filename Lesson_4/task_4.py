"""
Функция получает на вход список чисел. 
Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
Как вариант напишите сортировку пузырьком. 
Её описание есть в википедии.
"""

def sort_numbers(num_list: list)-> None:
    """Cортирует на месте. """
    for _ in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j]>num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1],num_list[j]


if __name__ == '__main__':
    lst = [int(i) for i in input("введите числа: ").split()]
    sort_numbers(lst)
    print(lst)