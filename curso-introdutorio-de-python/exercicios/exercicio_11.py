'''
FAÇA UM PROGRAMA QUE ITERA EM UMA STRING E TODA VEZ QUE UMA VOGAL APARECER NA
SUA STRING PRINT O NOME ENTRE AS LETRAS
EXEMPLO
string = babananas
b
eduardo
n
eduardo
n
'''

palavra = 'jjjjj'
vogais = 'aeiou'

#for letra in palavra:
#    if letra == 'a':
#        print('Jose')
#    elif letra == 'e':
#        print('Jose')
#    elif letra == 'i':
#        print('Jose')
#    elif letra == 'o':
#        print('Jose')
#    elif letra == 'u':
#        print('Jose')
#    else:
#        print(letra)

for letra in palavra:
    if letra in vogais:
        print('Jose')
    else:
        print(letra)
