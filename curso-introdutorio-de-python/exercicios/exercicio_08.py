'''
FAÇA UM PROGRAMA QUE RECEBA UMA DATA DE NASCIMENTO (15/07/87) E IMPRIMA
'VOCÊ NASCEU EM <DIA> DE <MÊS> DE <ANO>'
'''
resposta = input('Qual sua data de nascimento? ')

dia, mes, ano = resposta.split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}!!')
