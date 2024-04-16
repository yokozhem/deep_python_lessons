"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
def no_s():
    """Удаляет S из имен переменных."""
    lst = {}
    for var, val in globals().items():
        if var != "s" and var.endswith("s") and var != "no_s":
            lst[var[:-1]] = val
            globals()[var] = None
    for k,v in lst.items():
        globals()[k]= v 


if __name__ == '__main__':
    items = 0
    names = "dsdsd"
    s = 5
    value = "ffff"
    print(globals())
    no_s()
    print(globals())