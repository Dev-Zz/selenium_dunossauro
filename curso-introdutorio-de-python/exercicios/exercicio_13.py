'''
FAÇA UM PROGRAMA QUE: DADA UMA LISTA [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] E UM NÚMERO
INTEIRO, IMPRIMA A TABUADA DESSE NÚMERO.
'''

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resposta = int(input('Fale um número de 1 até 10: '))

for numero in lista_de_numeros:
    print(f'{numero} X {resposta} = {numero * resposta}')
