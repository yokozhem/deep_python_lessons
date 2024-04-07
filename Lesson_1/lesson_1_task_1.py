# Task 1
n = int(input("Введите число?"))
e = int(input("Введите число е?"))


def sum_of_even_excluding_multiples(n, e):
    sum_even = 0
    i = 1
    while i <= n:
        if i % 2 == 0 and i % e != 0:
            sum_even += i
        i += 1
    return sum_even

result = sum_of_even_excluding_multiples(n, e)
print("Сумма четных элементов от 1 до", n, "исключая кратные", e, "равна:", result)