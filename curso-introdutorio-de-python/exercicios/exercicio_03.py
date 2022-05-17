'''
FAÇA UM PROGRAMA PARA UMA LOJA DE TINTAS. O PROGRAMA DEVERÁ PEDIR O TAMANHO EM
METROS QUADRADOS DA ÁREA A SER PINTADA. CONSIDERE QUE A COBERTURA DA TINTA É DE
1 LITRO PARA CADA 3 METROS QUADRADOS E QUE A TINTA É VENDIDA EM LATAS DE 18
LITROS, QUE CUSTAM R$80,00. INFORME AO USUÁRIO A QUANTIDADE DE LATAS DE TINTA A
SEREM COMPRADAS E O PREÇO TOTAL.
'''

area = int(input('Qual o tamanho da área a ser pintada? '))
litros = (area / 3)

if(litros % 18) == 0:
    lata = (litros / 18)
else:
    lata = ((litros // 18) + 1)
    
valor_total = (lata * 80)

print(f'Vai ser necessário {lata} lata(s) de tinta, que custará {valor_total} reais')
