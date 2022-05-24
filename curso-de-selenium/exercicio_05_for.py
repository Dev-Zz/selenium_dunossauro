from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_05.html'
b.get(url)

def preenche_form(browser, context, nome, senha):
    sleep(1)
    context = browser.find_element_by_css_selector(f'.form-{form}')
    inputs_form = {
        'nome': context.find_element_by_css_selector('[type="text"]'),
        'senha': context.find_element_by_css_selector('[type="password"]'),
        'enviar': context.find_element_by_css_selector('[type="submit"]'),
    }

    inputs_form['nome'].send_keys(nome)
    inputs_form['senha'].send_keys(senha)
    inputs_form['enviar'].click()

forms = ['l0c0', 'l0c1', 'l1c0', 'l1c1']
for form in forms:
    preenche_form(b, form, 'Jose', 'Senha123')
