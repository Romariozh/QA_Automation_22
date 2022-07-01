# Є два довільних числа які відповідають за мінімальну і максимальну ціну. 
# Є Dict з назвами магазинів і цінами: { "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999,
# "main-service": 37.245, "buy.ua": 38.324, "my-store": 37.166, "the_partner": 38.988,
# "sto": 37.720, "rozetka": 38.003}. 
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон
# між мінімальною і максимальною ціною.

# Checking data input for a number
while True:
    try:
        min_val = float(input('Enter the minimum price -> '))
        max_val = float(input('Enter the maximum price -> '))
        break
    except ValueError:
        print('You entered not a number.')
        print('Tyr again!')

#There is a dict of shops and prices
markets = {
    'cilpio': 47.999,
    'a_studio': 42.999,
    'main-service': 37.245,
    'hws': 41.099,
    'buy.ua': 38.324,
    'my-store': 37.166,
    'my-petstore': 36.886,
    'the_partner': 38.988,
    'rozetka': 38.003,
    'sto': 37.720,
}

match = []

for key, value in markets.items():
    if min_val < value < max_val:
        match.append(key)
res = str(match)
print(f'> match: {res[1 : -1]}')
