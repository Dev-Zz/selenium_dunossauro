from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

b.find_elements_by_css_selector('div.form-group')
