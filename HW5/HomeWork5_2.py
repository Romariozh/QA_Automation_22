# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).

def convert_to_float(element):
    try:
        float(element)
        return float(element)
    except ValueError:
        return 0.0


test1 = convert_to_float(input('Enter the numeric: '))
print(test1)