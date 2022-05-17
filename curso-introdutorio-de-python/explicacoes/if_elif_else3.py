carteira = int(input('Quanto eu tenho na carteira? '))
tenis = int(input('Quanto custa? '))
necessidade = input('Preciso mesmo disso [S/N]? ')

if carteira >= tenis and necessidade == 'S':
    print('Luxei!')
else:
    print('Foi triste!')
