from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_05.html'

b.get(url)

classe = b.find_element_by_css_selector('form.form-l0c0')
nome = b.find_element_by_css_selector('[type="text"]').send_keys('Jose')
senha = b.find_element_by_css_selector('[type="password"]').send_keys('1643114#Ze')
sleep(1.5)
btn = b.find_element_by_css_selector('[type="submit"]').click()

classe = b.find_element_by_css_selector('form.form-l0c1')
nome = classe.find_element_by_css_selector('[type="text"]').send_keys('Josefson')
senha = classe.find_element_by_css_selector('[type="password"]').send_keys('1643114#Ze')
sleep(1.5)
btn = classe.find_element_by_css_selector('[type="submit"]').click()

classe = b.find_element_by_css_selector('form.form-l1c0')
nome = classe.find_element_by_css_selector('[type="text"]').send_keys('Josefson')
senha = classe.find_element_by_css_selector('[type="password"]').send_keys('1643114#Ze')
sleep(1.5)
btn = classe.find_element_by_css_selector('[type="submit"]').click()

classe = b.find_element_by_css_selector('form.form-l1c1')
nome = classe.find_element_by_css_selector('[type="text"]').send_keys('Josefson')
senha = classe.find_element_by_css_selector('[type="password"]').send_keys('1643114#Ze')
sleep(1.5)
btn = classe.find_element_by_css_selector('[type="submit"]').click()
