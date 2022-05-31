'''
Pegar todos os dados da PAGINA e mostrar para o usuario.

como resolver?

1 - Usar o .find_element_by_css_selector() para encontrar todos os dados.
2 - Entender como colocar isso dentro de uma variavel
3 - Mostrar isso na tela
'''

from time import sleep
from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(2)

dicionario = {}
h1 = browser.find_element_by_css_selector('h1').text
ps = browser.find_elements_by_css_selector('p')

for p in ps:
    dicionario.update({p.get_attribute('atributo'): p.text})
print({h1: dicionario})
