2 > 3 #Falso, Inverdade, False
3> 2 #Verdadeiro, True

type(True)
type(False)

nome_1 = 'Fausto'
idade_1 = 3
nome_2 = 'Maria'
idade_2 = 23
nome_3 = 'Fausto'
idade_3 = 45

nome_1 == nome_2 #False
nome_1 == nome_3 #True
nome_1 != nome_2 #True

compara_nomes = nome_1 == nome_3 and idade_1 == idade_3 #False
compara_nomes_or = nome_1 == nome_3 or idade_1 == idade_3 #True
