# Задача: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print('Addition: ', first + second, '\n' +
      'Subtraction: ', first - second, '\n' +
      'Multiplication: ', first * second, '\n' +
      'Division: ', first / second, '\n' +
      'Integer division: ', first // second, '\n')

# Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

my_bool = first < second
print('First < Second: ', my_bool)

my_bool = first > second
print('First > Second: ', my_bool)

my_bool = first == second
print('First == Second: ', my_bool)

my_bool = first != second
print('First != Second: ', my_bool, '\n')

# Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран.

str1 = 'Hello '
str2 = 'world'
summury = str1 + str2
print(summury)
