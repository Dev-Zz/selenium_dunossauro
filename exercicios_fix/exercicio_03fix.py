from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
#-----------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/exercicio_03.html'

def find_a_by_attr(browser, attr, val):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.get_attribute(attr) == val:
            return elemento

browser = Firefox()
browser.get(url)

#pag.1
sleep(0.7)
main = browser.find_element_by_tag_name('main')
main.find_element_by_tag_name('a').click()

#pag.2
sleep(0.7)
main = browser.find_element_by_tag_name('main')
find_a_by_attr(main, 'attr', 'errado').click()

#pag.3
sleep(30)
main = browser.find_element_by_tag_name('main')
titulo = browser.title
