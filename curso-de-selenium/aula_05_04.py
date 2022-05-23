from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_05.html'
browser = Firefox()
browser.get(url)
sleep(2)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

preenche_form(
    browser,
    'Jose Eduardo',
    'ejose798@gmail.com',
    '1643114#Ze',
    '(065)981020200',
)
