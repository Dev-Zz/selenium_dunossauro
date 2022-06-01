'''
Preencher o formulário e enviar.

URL = 'https://selenium.dunossauro.live/exercicio_04.html'

1 Passo - Abrir a pagina de forma automatica.
2 Passo - Encontrar todos os elementos input da pagina.
3 Passo - Criar a logica para que seja feito o .send_keys().
4 Passo - Clicar no Botão ENVIAR.

pag2

Pegar todos os dados digitados e cruzar com os dados da URL e comparar ambos.

1 Passo - Pegar todos os dados digitados
2 Passo - Pegar a URL atual
3 Passo - Separar a URL
4 Passo - URL == Text?
'''


from cgitb import text
from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl

#abrir a url
url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Firefox()
browser.get(url)

#pag1
sleep(1)
nome = browser.find_element_by_css_selector('[name="nome"]').send_keys('Jose')
email = browser.find_element_by_css_selector('[name="email"]').send_keys('zz-dev@outlook.com')
senha = browser.find_element_by_css_selector('[name="senha"]').send_keys('1643114Ze')
telefone = browser.find_element_by_css_selector('[name="telefone"]').send_keys('65981020200')
btn = browser.find_element_by_css_selector('[name="btn"]').click()

#pag2
sleep(1)
textarea = eval(browser.find_element_by_css_selector('textarea').text)
url_parse = dict(parse_qsl(urlparse(browser.current_url).query))
url_parse.pop('btn')

if textarea == url_parse:
    print('\n\nESTÁ TUDO IGUAL!!')