# Напишіть функцію, що приймає два аргументи. Функція повинна
# a. якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
# b. якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# c. якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# d. у будь-якому іншому випадку повернути кортеж з цих аргументів

# Function to define INT or FLOAT from input users data
def is_num(checking_string):
    if checking_string.isdigit():
        return True
    else:
        try:
            float(checking_string)
            return True
        except ValueError:
            return False


def arguments_conversion(elem1, elem2):
    if is_num(elem1) is True and is_num(elem2) is True:
        return float(elem1) - float(elem2)
    elif is_num(elem1) is False and is_num(elem2) is False:
        return elem1 + elem2
    elif is_num(elem1) is False and is_num(elem2) is True:
        return {elem1: float(elem2)}
    else:
        return elem1, elem2


# Checking user input for two non-empty arguments
while True:
    value_1, value_2 = input('Enter something (first): '), input('Enter something else (second): ')
    if len(value_1) != 0 and len(value_2) != 0:
        break
    else:
        print('You didn\'t enter two arguments. Try again.')

print(arguments_conversion(value_1, value_2))
