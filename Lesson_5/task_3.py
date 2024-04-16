"""
Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

import sys

text = "Самостоятельно сохраните в переменной строку текста."
dictionary = {key: ord(key) for key in text}
iterator = iter(dictionary.items())
print(iterator, type(iterator), sys.getsizeof(iterator), sys.getsizeof(dictionary))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('Начало цикла for')

iterator = iter(dictionary.items())  # Создаем итератор заново
for item in range(5):
    print(next(iterator))
