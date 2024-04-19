"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

from random import randint

def guess_number(lower_limit, upper_limit, count):
    n = randint(lower_limit, upper_limit)
    i = 1
    print(f"Компьютер загадал число. Отгадайте его. У вас {count} попыток")
    while i <= count:
        u = int(input(str(i) + '-я попытка: '))
        if u > n:
            print('Меньше')
        elif u < n:
            print('Больше')
        else:
            print('Вы угадали с %d-й попытки' % i)
            break
        i += 1
    else:
        print(f'Вы исчерпали {count} попыток. Было загадано', n)


if __name__=='__main__':
    lower_limit = int(input("Введите нижнюю границу: "))
    upper_limit = int(input("Введите верхнюю границу: "))
    count = int(input("Введите число попыток: "))

    guess_number(lower_limit, upper_limit, count)
