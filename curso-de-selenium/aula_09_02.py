from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait


def espera_botao(webdriver):
    elements = webdriver.find_elements_by_css_selector('button')
    print('Tentando encontrar "Button"')
    return bool(elements)

def espera_sucesso(webdriver):
    elements = webdriver.find_elements_by_css_selector('#finished')
    print('Aguardando Sucesso!"')
    return bool(elements)

url = 'https://selenium.dunossauro.live/aula_09_a.html'
browser = Firefox()
wdw = WebDriverWait(browser, 10, poll_frequency=0.5)
browser.get(url)
wdw.until(espera_botao)
browser.find_element_by_css_selector('button').click()
wdw.until(espera_sucesso)
print('-'*20)
print('DEU TUDO CERTO!')
browser.quit()