from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
#-----------------------------------------------------------------#
url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)

#----------------------------pagina um-------------------------------------#
sleep(1)
main = browser.find_element_by_tag_name('main')
main.find_element_by_tag_name('a').click()
#----------------------------pagina dois-----------------------------------#
sleep(1)
main = browser.find_element_by_tag_name('main')
main.find_element_by_css_selector('[href="page_2.html"]').click()
#----------------------------pagina tres-----------------------------------#
sleep(30)
main = browser.find_element_by_tag_name('main')
main.find_element_by_css_selector('[href="page_3.html"]').click()
#----------------------------pagina quatro---------------------------------#
sleep(1)
main = browser.find_element_by_tag_name('main')
main.find_element_by_css_selector('[href="page_4.html"]').click()
#----------------------------pagina quatro---------------------------------#
sleep(1)
browser.refresh()
#----------------------------FIM-------------------------------------------#
