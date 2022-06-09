'''Escreva um algoritimo que termine o JOGO das Páginas'''


from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)


#pag1
sleep(2)
browser.find_element_by_css_selector('[href="page_1.html"]').click()
#pag2
sleep(2)
browser.find_element_by_css_selector('[href="page_2.html"]').click()
#pag3
sleep(2)
browser.find_element_by_css_selector('[href="page_3.html"]').click()
#pag4
sleep(2)
browser.find_element_by_css_selector('[href="page_4.html"]').click()
#pag5
sleep(2)
browser.refresh()

print('VOCÊ GANHOU!!!!!!!')
sleep(2)
browser.quit()