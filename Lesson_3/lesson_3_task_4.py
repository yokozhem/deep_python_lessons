""" Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""

from collections import Counter

lst = [1, 1, 1, 5, 4, 7, 7, 8, 9, 9, 10]
dic2 = Counter(lst) # + сортирует по убыванию счетчиков!
dic = {}
for item in lst:
    if item not in dic:
        dic[item] = 0
        dic[item] += 1 # dct[el] = dct.get(el, 0)
for k, v in dic.items():
    if v == 2:
        lst.remove(k) # remove удаляет только одно вхождение!
        lst.remove(k)
print(lst)
print(dic)
print(dic2)