'''
Exercicio 1 - Pegar todos os links de aulas.
Exercicio 2 - Navegar até o Exercicio 3.
'''
#-------------------------------------------------------------#

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

#-------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/aula_04.html'
browser = Firefox()
browser.get(url)
sleep(2)

#-------------------------------------------------------------#
#Parte 1
#-------------------------------------------------------------#

'''
Pega todos os links dentro de um elemento
- browser = Instancia do navegador
- element = Webelement [aside, main, body]
'''

def get_links(browser, elemento): #dicionario

    result = {}
    element = browser.find_element_by_tag_name(elemento)
    links = element.find_elements_by_tag_name('a')
    for link in links:
        result[link.text] = link.get_attribute('href')
    return result

pprint(get_links(browser, 'aside'))
#-------------------------------------------------------------#
#Parte 2
#-------------------------------------------------------------#

exercicios = get_links(browser, 'main')
pprint(exercicios)
browser.get(exercicios['Exercício 3'])

#-------------------------------------------------------------#
