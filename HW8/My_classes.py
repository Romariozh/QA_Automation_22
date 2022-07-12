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
        if age_string % 10 in gradient_str_age[key] and age_string % 100 not in (11, 12, 13, 14):
            string_add_age = key
            break
    return string_add_age

def cinema_cashier(client_age: int) -> str:
    string_add_age = determ_age_in_str(client_age)
    # For create list of nice age like 11, 22, 33, 44 .... to 999
    element = 11
    nice_age = []
    while element <= 1000:
        nice_age.append(element)
        element += 11
        if element % 10 == 0:
            element += 1
        if element > 111:
            element += 100
    # checking conditions according to the task + answer for very old people
    if client_age in nice_age:
        response = 'О, вам {} {}! Який цікавий вік!'
    elif client_age < 7:
        response = 'Тобі ж {} {}! Де твої батьки?'
    elif client_age < 16:
        response = 'Тобі лише {} {}, а це фільм для дорослих!'
    elif client_age <= 65:
        response = 'Незважаючи на те що вам {} {}, білетів всеодно нема!'
    elif 65 < client_age < 100:
        response = 'Вам {} {}? Покажіть пенсійне посвідчення!'
    else:
        response = 'Вам {} {}, відвідування кінотеатру небезбечно для вашого здоров\'я!'
    return response.format(str(client_age), string_add_age)