from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

# usando a atributo 'type' [attr=valor]
# nome = b.find_element_by_css_selector('[type="text"]')
# nome = b.find_element_by_css_selector('[type="password"]')
# nome = b.find_element_by_css_selector('[type="submit"]')

# usando a atributo 'name' [attr=valor]
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# usando a atributo * [att*=valor]
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha  = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="c0"]')

# usando a atributo [att*=valor]
nome = b.find_element_by_css_selector('[name*="ome"]')
senha  = b.find_element_by_css_selector('[name*="nha"]')
btn = b.find_element_by_css_selector('[name*="c0"]')

nome.send_keys('Jose Eduardo')
senha.send_keys('1643114#Ze')
sleep(2)
btn.click()
