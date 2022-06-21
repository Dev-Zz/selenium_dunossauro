'''Escreva um algoritimo que termine o JOGO das Páginas'''


from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


def espera_pag1(webdriver):
    elements = webdriver.find_elements_by_css_selector('#main > h1:nth-child(1)')
    print('Tentando encontrar "Você está no Exercicio 03"')
    return bool(elements)

def espera_pag2(webdriver):
    elements = webdriver.find_elements_by_css_selector('#main > h1:nth-child(1)')
    print('Tentando encontrar "Você está na página 1"')
    return bool(elements)  

def espera_pag3(webdriver):
    elements = webdriver.find_elements_by_css_selector('#main > h1:nth-child(1)')
    print('Tentando encontrar "Você está na página 2"')
    return bool(elements)  

def espera_pag4(webdriver):
    elements = webdriver.find_elements_by_css_selector('#main > h1:nth-child(1)')
    print('Tentando encontrar "Você está na página 3"')
    return bool(elements)  

def espera_pag5(webdriver):
    elements = webdriver.find_elements_by_css_selector('#main > pre:nth-child(2)')
    print('Aguardando o DIABAO APARECER')
    return bool(elements)


url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
wdw = WebDriverWait(browser, 10, poll_frequency=0.5)
browser.get(url)


#pag1
wdw.until(espera_pag1)
browser.find_element_by_css_selector('[href="page_1.html"]').click()
#pag2
wdw.until(espera_pag2)
browser.find_element_by_css_selector('[href="page_2.html"]').click()
#pag3
wdw.until(espera_pag3)
browser.find_element_by_css_selector('[href="page_3.html"]').click()
#pag4
wdw.until(espera_pag4)
browser.find_element_by_css_selector('[href="page_4.html"]').click()
#pag5
wdw.until(espera_pag5)
browser.refresh()
print('VOCÊ GANHOU!!!!!!!')
sleep(2)
browser.quit()