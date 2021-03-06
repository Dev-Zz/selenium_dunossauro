from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_06.html'
b.get(url)
sleep(5)

def preenche_form(browser, form, nome, senha):
    context = browser.find_element_by_css_selector(f'.form-{form}')
    inputs_form = {
        'nome': context.find_element_by_css_selector('[type="text"]'),
        'senha': context.find_element_by_css_selector('[type="password"]'),
        'enviar': context.find_element_by_css_selector('[type="submit"]'),
    }

    inputs_form['nome'].send_keys(nome)
    inputs_form['senha'].send_keys(senha)
    inputs_form['enviar'].click()


for n in range(6):
    form = b.find_element_by_css_selector('span').text
    sleep(5)
    preenche_form(b, form, f'Jose{n}', f'Senha123{n}')
