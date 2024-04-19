"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.

"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_date(date):
    day, month, year = map(int, date.split('.'))
    max_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12 and 1 <= day <= max_days[month - 1]:
        return True, is_leap_year(year)
    else:
        return False, is_leap_year(year)

def main():
    date = input("Введите дату в формате DD.MM.YYYY: ")
    valid, leap = check_date(date)
    if valid:
        print("Допустимая дата")
        if leap:
            print("Год является високосным")
        else:
            print("Год не является високосным")
    else:
        print("Недопустимая дата")

if __name__ == "__main__":
    main()
