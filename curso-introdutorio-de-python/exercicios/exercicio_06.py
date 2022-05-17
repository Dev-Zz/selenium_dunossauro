'''
FAÇA UM PROGRAMA QUE PERGUNTE O PREÇO DE TRÊS PRODUTOS E INFORME QUAL
PRODUTO VOCÊ DEVE COMPRAR, SABENDO QUE A DECISÇÃO É SEMPRE PELO MAIS BARATO
'''

produto_1 = float(input('Qual o preço do copo? '))
produto_2 = float(input('Qual o preço da caneta? '))
produto_3 = float(input('Qual o preço do lapiz? '))

if produto_1 > produto_2 and produto_2 > produto_3:
    print('Compre o lapiz!!')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('Compre a caneta!!')
else:
    print('Compre o copo!!')
