# 2. Ввести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

enter_string = input('Please enter your sentence: ')
enter_string = enter_string.strip(' ')
list_str = enter_string.split(' ')

num_words = 0
for words in list_str:
    if words.isnumeric() is False and words != '':
        num_words += 1
        print(f'Word {num_words} is: {words}')
print('---------------')
print(f'In your sentence the numbers of words is: {num_words}')