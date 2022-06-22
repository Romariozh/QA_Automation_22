# 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

msg_try_again = 'Try again!'
str_word = input('Please enter a word: ')
length_word = len(str_word)
msg_available_symbol = f'Available symbol values form 1 to {length_word}'

str_num_symbol = input('Please enter a symbol number in the word: ')

if length_word != 0 and len(str_num_symbol) != 0:
    if str_num_symbol.isdigit():
        num_symbol = int(str_num_symbol)
        if len(str_word) >= num_symbol != 0:
            letter = str_word[num_symbol - 1]
            print(f'The {num_symbol} symbol in \"{str_word}\" is \'{letter}\'')
            print('Bingo!')
        elif num_symbol == 0:
            print('Symbol numbering starts from 1, not ZERO.')
        else:
            print(f'In the word \"{str_word}' +
                  f'\" missing symbol number {num_symbol}')
            print(msg_available_symbol)
            print(msg_try_again)
    else:
        print(msg_available_symbol)
        print(msg_try_again)
else:
    print('You didn\'t enter the word or symbol number!')

