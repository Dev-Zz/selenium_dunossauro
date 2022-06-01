'''
Preencher o formulário
'''

from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl


url = 'https://curso-python-selenium.netlify.app/exercicio_04.html'
browser = Firefox()
browser.get(url)

#PAGINA1
sleep(1.5)
#form-como podemos chamar você:
nome = browser.find_element_by_css_selector('[name="nome"]').send_keys('Jose')
#form-email:
email = browser.find_element_by_css_selector('[name="email"]').send_keys('ejose798@gmail.com')
#form-senha:
senha = browser.find_element_by_css_selector('[name="senha"]').send_keys('1643114')
#form-telefone:
telefone = browser.find_element_by_css_selector('[name="telefone"]').send_keys('65981020200')
#enviar
enviar = browser.find_element_by_css_selector('[name="btn"]').click()

#PAGINA2
sleep(1.5)
#pegar o texto
textarea = eval(browser.find_element_by_css_selector('textarea').text)
#pegar a url
url_atual = browser.current_url
url_organizada = dict(parse_qsl(urlparse(url_atual).query))
url_organizada.pop('btn')

if textarea == url_organizada:
    print('ESTÁ TUDO CERTO!!!')
else:
    print('NÃO ESTÁ IGUAL!!!')

