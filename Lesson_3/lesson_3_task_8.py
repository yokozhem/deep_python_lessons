""" Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

dic_things = {
    "Юра": ("палатка", "рюкзак", "котелок"),
    "Сергей": ("рюкзак", "палатка", "спички", "лопата"),
    "Олег": ("стол", "рюкзак", "продукты"),
}

if dic_things:
    first = next(iter(dic_things.keys()))  # Получаем первого человека из словаря
    res = set(dic_things[first])
    for v in dic_things.values():
        res = res.intersection(set(v))
    print("У всех есть - ", *res)

    dic_count = {}
    for v in dic_things.values():
        for item in v:
            dic_count[item] = dic_count.get(item, 0) + 1

    friends = len(dic_things) - 1
    missing_things = []
    for item, count in dic_count.items():
        if count < friends:
            missing_things.append(item)
    
    for name, things in dic_things.items():
        missing = [item for item in missing_things if item not in things]
        if missing:
            print(f"{', '.join(missing)} нет у {name}!")

    one_thing = [item for item, count in dic_count.items() if count == 1]
    print("Вещи в единственном экземпляре: ", *one_thing)
else:
    print("Словарь dic_things пуст!")
