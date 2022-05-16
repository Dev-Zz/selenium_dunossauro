from selenium.webdriver import Firefox
from time import sleep

#-------------------------------------------------------------#

def find_by_text(browser, tag, text):
    '''
    Encontrar o elemento com o texto ´text´
        Argumentos:
            - browser = Instancia do browser [Firefox, Chrome, ...]
            - texto = Conteúdo que deve estar na tag
            - tag = tag onde o texto será procurado
    '''
    elements = browser.find_elements_by_tag_name(tag) #lista

    for element in elements:
        if element.text == text:
            return element

#-------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/aula_04_b.html'
browser = Firefox()
browser.get(url)
sleep(1)

#-------------------------------------------------------------#

box_names = ['um', 'dois', 'tres', 'quatro']

for name in box_names:
    find_by_text(browser, 'div',  name).click()

for name in box_names:
    sleep(0.5)
    browser.back()

for name in box_names:
    sleep(0.5)
    browser.forward()

#-------------------------------------------------------------#
