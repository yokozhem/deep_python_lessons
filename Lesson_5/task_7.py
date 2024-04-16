"""
Создайте функцию-генератор.
Функция генерирует N простых чисел,
начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».
"""
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_simple():
    n = 2
    while True:
        if prime(n):
            yield n
        n += 1

if __name__ == "__main__":
    j = generate_simple()
    for _ in range(int(input("Введите число N: "))):
        print(next(j))
