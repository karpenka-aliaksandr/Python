n_min=1
n_max=100


while True:
    n = int ((n_min+n_max)/2)
    symbol=input(f'Ваше число - {n}? ')
    if symbol == '=':
        break;
    if symbol == '>':
        n_min = n+1
    if symbol == '<':
        n_max = n
print(f'Ура, ваше число {n}.')