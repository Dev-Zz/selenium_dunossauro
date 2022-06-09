'''Pegar todos os dados da pagina e colocar em um DICT'''

from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_01.html'
browser = Firefox()
browser.get(url)

sleep(2)
h1 = browser.find_element_by_css_selector('h1').text
ps = browser.find_elements_by_css_selector('p')
dicionario = {}

for p in ps:
    dicionario.update({p.get_attribute('atributo'): p.text})
print('h1= {}, {}'.format(h1, dicionario))