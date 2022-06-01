'''
Pegar todos os dados da PAGINA e mostrar para o usuario.

como resolver?

 - Verificar o que precisará importar das Library
 - Criar o script para abrir a URL
 - Usar o .find_element_by_css_selector() para encontrar todos os dados
 - Entender como colocar isso dentro de uma variavel
 - Colocar dentro de uma variavel
 - Mostrar isso na tela de forma organizada
'''
from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_01.html'
browser = Firefox()
browser.get(url)

#pag1
sleep(2)
h1 = browser.find_element_by_css_selector('h1').text
ps = browser.find_elements_by_css_selector('p')
dicionario = {}

for p in ps:
    dicionario.update({p.get_attribute('atributo'): p.text})

print('h1= {}, {}'.format(h1, dicionario))

