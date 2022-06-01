'''
FAÇA UM SCRIPT QUE JOGUE O JOGO.

URL: 'https://selenium.dunossauro.live/exercicio_03.html'

1 - Faça um script que abra a URL.
2 - Busque os valores de cada elemento de cada pagina para passar pagina por pagina.
3 - Interaja com o Elemento de pagina por pagina.
'''

from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)


#pag1
sleep(1)
page1 = browser.find_element_by_css_selector('[href="page_1.html"]').click()

#pag2
sleep(1)
page2 = browser.find_element_by_css_selector('[href="page_2.html"]').click()

#pag3
sleep(30)
page3 = browser.find_element_by_css_selector('[href="page_3.html"]').click()

#pag4
sleep(1)
page4 = browser.find_element_by_css_selector('[href="page_4.html"]').click()

#pag5
sleep(1)
browser.refresh()




