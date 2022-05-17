'''
Faça um programa que peça 2 números inteiros e 1 número float. Calcule e mostre:

    O produto do dobro do primeiro com metade do segundo.
    A soma do triplo do primeiro com o terceiro.
    O terceiro elevado ao cubo.
'''

primeiro = int(input('Digite um número INTEIRO: '))
segundo = int(input('Digite outro número INTEIRO: '))
terceiro = float(input('Digite um número FLOAT:  '))

resp1 = (primeiro * 2) * (segundo / 2)
resp2 = (primeiro * 3) + terceiro
resp3 = terceiro ** 3

print(resp1)
print(resp2)
print(resp3)
