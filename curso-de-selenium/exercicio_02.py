from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
#----------------------------------------------------------------------#

'''
Exercicio 02
    Jogue o jogo.
    Rode o Script até ganhar no jogo.
'''

#----------------------------------------------------------------------#

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Firefox()
browser.get(url)
sleep(1)
a = browser.find_element_by_tag_name('a')
resultado = 'Você ganhou'
msg = ''

while resultado not in msg:
    a.click()
    msg = browser.find_elements_by_tag_name('p')[-1].text

#----------------------------------------------------------------------#
