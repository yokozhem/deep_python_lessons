"""
Самостоятельно сохраните в переменной строку текста. 
Создайте из строки словарь, где ключ — буква, а значение — код буквы. 
Напишите преобразование в одну строку. 

"""

text = 'Без труда не вытащишь и рыбку из пруда!'
print({key: ord(key) for key in text})