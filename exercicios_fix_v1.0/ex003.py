'''
FAÇA UM SCRIPT QUE JOGUE O JOGO.

URL: 'https://selenium.dunossauro.live/exercicio_03.html'

1 - Faça um script que abra a URL.
2 - Busque os valores de cada elemento de cada pagina para passar pagina por pagina.
3 - Interaja com o Elemento de pagina por pagina.
'''

from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)

#pag1
sleep(2)
main = browser.find_element_by_css_selector('main')
a = main.find_element_by_css_selector('a')
a.click()

#pag2
sleep(2)
main = browser.find_element_by_css_selector('main')
a = main.find_element_by_css_selector('[href="page_2.html"]')
a.click()

#pag3
sleep(30)
main = browser.find_element_by_css_selector('main')
a = main.find_element_by_css_selector('[href="page_3.html"]')
a.click()

#pag4
sleep(2)
main = browser.find_element_by_css_selector('main')
a = main.find_element_by_css_selector('[href="page_4.html"]')
a.click()

#pag5
sleep(2)
browser.refresh()
