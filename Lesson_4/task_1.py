"""
Напишите функцию, которая принимает строку текста. 
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого 
длинного слова был один пробел между ним и номером строки. """

def prin_text(text: str):
    text_lst = text.split()
    text_lst.sort()

    max_len = max([len(word) for word in text_lst])
    max_len1 = len(max(text_lst, key=len))

    for i, word in enumerate(text_lst, 1):
        print(f'{i} {word:>{max_len}}')

if __name__=='_main_':
    prin_text(input("Введите текст: "))