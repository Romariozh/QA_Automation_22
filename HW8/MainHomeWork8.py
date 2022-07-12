# Візьміть свою HW 6 ("Касир в кінотеатрі"), винесіть всі допоміжні функціі в окремий файл.
# В основному файлі виконайте імпорт цих функцій.
from My_classes import cinema_cashier as cashier


while True:
    try:
        age = int(input('Enter you age -> '))
        if 1 <= age != 0:
            break
        else:
            print('Incorrect entered your age. Try again.')
    except ValueError:
        print('You entered not a integer. Tyr again!')

if __name__ == "__main__":
    print(cashier(age))