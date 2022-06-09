from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl


url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Firefox()
browser.get(url)

#pag1
sleep(2)
nome = browser.find_element_by_css_selector('[name="nome"]')
sleep(0.5)
nome.send_keys('Jose')
email = browser.find_element_by_css_selector('[name="email"]')
sleep(0.5)
email.send_keys('ejose798@gmail.com')
senha = browser.find_element_by_css_selector('[name="senha"]')
sleep(0.5)
senha.send_keys('1643114')
telefone = browser.find_element_by_css_selector('[name="telefone"]')
sleep(0.5)
telefone.send_keys('65981020200')
sleep(0.5)
btn = browser.find_element_by_css_selector('[name="btn"]').click()

#pag2
sleep(2)
current_url = browser.current_url
text = browser.find_element_by_css_selector('textarea').text
text = eval(text)
current_url = urlparse(current_url)
current_url = current_url.query
current_url = parse_qsl(current_url)
current_url = dict(current_url)
current_url.pop('btn')

print(f'\n\n CURRENT URL: {current_url}')
print(f' TEXAREA: {text}')
print('\n\n\n')
if text == current_url:
    print('DEU TUDO CERTO!')
else:
    print('DEU TUDO ERRADO!')