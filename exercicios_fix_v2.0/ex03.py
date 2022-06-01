'''Faça um algoritmo que jogue o jogo das paginas'''


from selenium.webdriver import Firefox
from time import sleep


url = 'https://curso-python-selenium.netlify.app/exercicio_03.html'
browser = Firefox()
browser.get(url)

#pag1
sleep(1.5)
browser.find_element_by_css_selector('[href="page_1.html"]').click()
#pag2
sleep(1.5)
browser.find_element_by_css_selector('[href="page_2.html"]').click()
#pag3
sleep(30)
browser.find_element_by_css_selector('[href="page_3.html"]').click()
#pag4
sleep(1.5)
browser.find_element_by_css_selector('[href="page_4.html"]').click()
#pag5
browser.refresh()