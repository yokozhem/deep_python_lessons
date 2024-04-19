"""
Создайте пакет с всеми модулями, которые вы создали за время занятия. 
Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

"""

# __init__.py
__all__ = ["module1", "module2", "module3"]

# module1.py
__all__ = ["function1", "function2"]

def function1():
    pass

def function2():
    pass

def internal_function():
    pass

# module2.py
__all__ = ["function3"]

def function3():
    pass

def internal_function():
    pass

# module3.py
__all__ = ["function4", "function5"]

def function4():
    pass

def function5():
    pass

def internal_function():
    pass
