'''
Faça um programa que pegue todos os dados da página e mostre para na tela.

Como resolver?

step 1 - Abrir a página de forma automatica 'OK'.
step 2 - Entender todos os dados que tem na pagina.
step 3 - Entender qual função usará para pegar os dados.
step 4 - Colocar os dados dentro de uma váriavel.
step 5 - Criar o dicionário para mostrar esses dados.
step 6 - Printar esses dados.
'''

from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(2)

h1 = browser.find_element_by_css_selector('h1').text
ps = browser.find_elements_by_css_selector('p')
dicionario = {}

#for p in ps:
#    dicionario.update({p.get_attribute('atributo'): p.text})
#print(h1, dicionario)

for p in ps:
    print(p.get_attribute('atributo'), p.text)