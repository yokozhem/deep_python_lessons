""" Пользователь вводит строку текста.
Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке.
Обратите внимание на порядок ключей. Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

from collections import Counter

str_user = input("Введите строку: ")
dic = {}
for letter in str_user:
    dic[letter] = str_user.count(letter)
print(Counter(str_user))
print(dic)