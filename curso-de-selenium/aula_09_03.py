from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def esperar_elemento(elemento, webdriver):
    print(f'Tentando encontrar "{elemento}"')
    if webdriver.find_elements_by_css_selector(elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

url = 'https://selenium.dunossauro.live/aula_09_a.html'
browser = Firefox()
wdw = WebDriverWait(browser, 10)
browser.get(url)

wdw.until(esperar_botao, 'Botão não APARECEU!')
browser.find_element_by_css_selector('button').click()

wdw.until(esperar_sucesso, 'Mensagem sucesso não apareceu.')
sucesso = browser.find_element_by_css_selector('#finished')

if sucesso.text == 'Carregamento concluído':
    print('Deu CERTO!')
else:
    print('Algo deu ERRADO!')

sleep(2)
browser.quit()