"""
Создайте генератор чётных чисел от нуля до 100. 
Из последовательности исключите числа, сумма цифр которых равна 8. 
Решение в одну строку.

"""

even_numbers_generator = (num for num in range(0, 101, 2) if sum(int(digit) for digit in str(num)) != 8)
print(*("FizzBuzz" if i % 3 == 0 and i % 5 == 0
else "Fizz" if i % 3 == 0
else "Buzz" if i % 5 == 0
else i
for i in range(1,101)))