'''Crie um loop para jogar o jogo da pagina'''

from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_02.html'
browser = Firefox()
browser.get(url)

sleep(2)
msg = ''
a = browser.find_element_by_css_selector('[id="ancora"]')
while True:
    a.click()
    msg = browser.find_elements_by_css_selector('p')[-1].text
    if 'Você ganhou' in msg:
        break
print('='*100)
print('O PROGRAMA ACABOU!!!!!!!!!!!!')   
print('='*100)