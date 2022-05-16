from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By

#mode headless
#------------------------------------------------------------------------#
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(2)

ps = browser.find_elements_by_tag_name('p')
h1 = browser.find_element_by_tag_name('h1').text
dicionario_de_atributos = {}

for p in ps:
    dicionario_de_atributos.update(
        {p.get_attribute('atributo'): p.text}
    )

print({h1: dicionario_de_atributos})
