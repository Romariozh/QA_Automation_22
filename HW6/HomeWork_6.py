# Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О,
# вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"

# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
# Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.

def determ_age_in_str(age_string: int) -> str:
    """
    The function determines the age and returns a string describing the age like 'рік', 'роки', 'років'
    """
    gradient_str_age = {
        'рік': (1, 1),
        'роки': (2, 3, 4),
    }
    string_add_age = 'років'
    for key in gradient_str_age.keys():
        if age_string % 10 in gradient_str_age[key] and age_string not in (11, 12, 13, 14):
            string_add_age = key
            break
    return string_add_age

def cinema_cashier(client_age: int) -> str:
    string_add_age = determ_age_in_str(client_age)
    # For create list of nice age from 11 to 999
    element = 11
    nice_age = []
    while element <= 1000:
        nice_age.append(element)
        element += 11
        if element % 10 == 0:
            element += 1
    # checking conditions according to the task + answer for very old people
    if client_age in nice_age:
        response = f'О, вам {str(client_age)} {string_add_age}! Який цікавий вік!'
    elif client_age < 7:
        response = f'Тобі ж {str(client_age)} {string_add_age}! Де твої батьки?'
    elif client_age < 16:
        response = f'Тобі лише {str(client_age)} {string_add_age}, а це фільм для дорослих!'
    elif client_age <= 65:
        response = f'Незважаючи на те що вам {str(client_age)} {string_add_age}, білетів всеодно нема!'
    elif 65 < client_age < 100:
        response = f'Вам {str(client_age)} {string_add_age}? Покажіть пенсійне посвідчення!'
    else:
        response = f'Вам {str(client_age)} {string_add_age}, відвідування кінотеатру небезбечно для вашого здоров\'я!'
    return response


while True:
    try:
        age = int(input('Enter you age -> '))
        if 1 <= age != 0:
            break
        else:
            print('Incorrect entered your age. Try again.')
    except ValueError:
        print('You entered not a integer. Tyr again!')

print(cinema_cashier(age))
