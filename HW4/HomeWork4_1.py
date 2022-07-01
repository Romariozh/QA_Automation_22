# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран 
# кількість слів, які містять дві голосні літери підряд.

vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

enter_string = input('Please enter your sentence: ')
enter_string = enter_string.strip(' ')
list_str = enter_string.split(' ')
letter_lst = list()

count_right_word = 0

for word in list_str:
    if word != '':
        word_lst = list(word)
        # auxiliary meter
        k = 0
        for elem in word_lst:
            if elem in vowels:
                k += 1
            else:
                k = 0
            if k == 2:
                count_right_word += 1
                print(f'Word "{word}" has more than two vowels at a stretch.')
        letter_lst = list()

print('--------------------------------------------------')
print(f'The sentence contains words with two vowels in a row.')
print(f'Quantity is {count_right_word}')
