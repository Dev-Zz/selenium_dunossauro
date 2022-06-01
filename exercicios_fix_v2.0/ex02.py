'''Exercicio 02
    Jogue o jogo.
    Rode o Script até ganhar no jogo.

URL = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

COMO RESOLVER?

STEP 1 - Faça um script que abra a URL.
STEP 2 - Faça um script que click no notão 'Clique aqui'.
STEP 3 - Faça um script que clique no botão até que apareça a mensagem: Você ganhou.'''

from selenium.webdriver import Firefox
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Firefox()
browser.get(url)
sleep(2)

#pag1
a = browser.find_element_by_css_selector('[id="ancora"]').click()
p = browser.find_elements_by_css_selector('p')[-1].text
msg = ''
result = 'Você ganhou'

while result not in msg:
    browser.find_element_by_css_selector('[id="ancora"]').click()
    msg = browser.find_elements_by_css_selector('p')[-1].text