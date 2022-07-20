# Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
# Певернути колекцію, кожен член якої є перетвореним членом вхідної колекції.
#
# Нотатка. Обʼєкт функції, яку передаємо вказує на функцію, котра приймає один аргумент.
# Не користуватися функціями map чи filter!!!
import math


def my_fun(fun, coll) -> list:
    create_coll = list()
    for item in coll:
        create_coll.append(fun(item) / (2 * item))
    return create_coll


if __name__ == '__main__':
    collect = (0.01, 0.02, 0.1, 0.2, 0.4, 0.7, 0.9, 1, 2, 2.8, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111)
    result = my_fun(math.log10, collect)
    print('Result: ', result)
