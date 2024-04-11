""" Функция принимает на вход три списка одинаковой длины:
имена str, 
ставка int, 
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой 
премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии.
"""
def calculate_bonus(names: list[str], rates: list[int], percents: list[str]) -> dict:
    """Расчет премии."""
    calculation = {}
    for name, rate, percent in zip(names, rates, percents):
        percent = float(percent[:-1])
        calculation[name] = rate * percent/100
    return calculation


if __name__ == '__main__':
    names = ["Oleg", "Vladimir", "Anton"]
    rates = [60_000, 75_000, 85_000]
    percents = ['10.25%', '8.0%', '4.5%']
    print(calculate_bonus(names, rates, percents))