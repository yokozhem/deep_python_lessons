"""
Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

"""


def guess_riddle(riddle, options, attempts):
    """
    Функция для отгадывания загадок.

    Args:
        riddle (str): Загадка.
        options (list): Список с возможными вариантами отгадок.
        attempts (int): Количество попыток на угадывание.

    Returns:
        int: Номер попытки, с которой была отгадана загадка,
             или 0, если попытки исчерпаны.
    """
    print("Угадайте загадку:")
    print(riddle)

    for i in range(1, attempts + 1):
        print(f"Попытка № {i}:")
        guess = input("Введите свой вариант: ").lower()

        if guess in options:
            print("Поздравляем! Вы угадали!")
            return i

        print("Неверный ответ. Попробуйте еще раз.")

    print("Попытки исчерпаны. Загадка не отгадана.")
    return 0