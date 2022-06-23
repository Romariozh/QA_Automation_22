# 3. Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

list_main = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(f'This is original list  {list_main}')

list_result = list()

for elem in list_main:
    if type(elem) == int:
        next_elem = int(elem)
        list_result.append(next_elem)
    elif type(elem) == float:
        next_elem = float(elem)
        list_result.append(next_elem)
    elif type(elem) == str and elem != '' and elem.isdigit():
        next_elem = int(elem)
        list_result.append(next_elem)

print(f'In this list was included only numeric variables {list_result}')