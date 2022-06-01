'''
Faça um script que preencha os 4 formulários.

URL = 'http://selenium.dunossauro.live/exercicio_05.html'

1 - pegar o identficador de formulário
2 - encontrar o input de cada formulário
3 - enviar inputs para os formulários
4 - criar a logica que faça o envio de todos os formulários
'''

from selenium.webdriver import Firefox
from time import sleep

def preenche_form(context, nome, senha):
    input_form = {
        'nome': context.find_element_by_css_selector('[type="text"]'),
        'senha': context.find_element_by_css_selector('[type="password"]'),
        'enviar': context.find_element_by_css_selector('[type="submit"]'),
    }
    
    input_form['nome'].send_keys(nome)
    input_form['senha'].send_keys(senha)
    input_form['enviar'].click()

#abrir a url
url = 'http://selenium.dunossauro.live/exercicio_05.html'
browser = Firefox()
browser.get(url)
sleep(1)

#pag1
sleep(0.7)
l0c0 = browser.find_element_by_css_selector('[class="form-l0c0"]')
preenche_form(l0c0, 'Jose', '123456')
sleep(0.7)
l0c1 = browser.find_element_by_css_selector('[class="form-l0c1"]')
preenche_form(l0c1, 'Jose1', '1234561')
sleep(0.7)
l1c0 = browser.find_element_by_css_selector('[class="form-l1c0"]')
preenche_form(l1c0, 'Jose2', '1234562')
sleep(0.7)
l1c1 = browser.find_element_by_css_selector('[class="form-l1c1"]')
preenche_form(l1c1, 'Jose3', '1234564')