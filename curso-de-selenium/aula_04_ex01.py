from selenium.webdriver import Firefox
#--------------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/aula_04_a.html'
browser = Firefox()
browser.get(url)
lista_n_ordenada = browser.find_element_by_tag_name('ul')
