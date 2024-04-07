""" Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег """

from decimal import Decimal

# Constants
PROCENT_COMMISION = Decimal('0.015')  # Commission as a percentage
MIN_SUM = Decimal('50')  # Minimum sum
MIN_COMISSION = Decimal('30')  # Minimum commission
MAX_COMISSION = Decimal('600')  # Maximum commission


def get_money(balance: Decimal) -> Decimal:
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств для снятия')
            return balance

    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50')
        return balance


def give_money(balance: Decimal) -> Decimal:
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        return balance + money_to_give
    else:
        print('Недостаточно средств для пополнения, сумма не кратна 50')
        return balance


def menu():
    print("1. Пополнить счет")
    print("2. Снять деньги")
    print("3. Выйти")


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат')
    balance = Decimal('0')
    isFlag = True
    while isFlag:
        menu()
        choice = input('Выберите действие: ')
        if choice == '1':
            balance = give_money(balance)
        elif choice == '2':
            balance = get_money(balance)
        elif choice == '3':
            print('До свидания!')
            isFlag = False
        else:
            print('Некорректный выбор. Пожалуйста, выберите снова.')
