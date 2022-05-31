from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
#-----------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(0.7)

#-----------------------------------------------------------------#

h1 = browser.find_element_by_tag_name('h1').text
ps = browser.find_elements_by_tag_name('p')
dicionario_de_atributos = {}

for p in ps:
    dicionario_de_atributos.update(
    {p.get_attribute('atributo'): p.text}
    )

print({h1: dicionario_de_atributos})
