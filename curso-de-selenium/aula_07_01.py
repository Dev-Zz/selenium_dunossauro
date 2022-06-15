'''
Chegar se a mudança occorre no span (focus, blur)
Checar se a mudança ocorre no p (change)
'''

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_07_d.html'
browser.get(url)

sleep(2)
input_text = browser.find_element_by_css_selector('input')
span = browser.find_element_by_css_selector('span')
browser.find_element_by_css_selector('p')
sleep(0.5)
input_text.click()
print(span.text)