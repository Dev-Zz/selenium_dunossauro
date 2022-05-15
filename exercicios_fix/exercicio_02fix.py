from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
#-----------------------------------------------------------------#

url = 'https://selenium.dunossauro.live/exercicio_02.html'
browser = Firefox()
browser.get(url)
sleep(0.7)

#-----------------------------------------------------------------#

a = browser.find_element_by_tag_name('a')
result = 'Você ganhou'
msg = ''

while result not in msg:
    a.click()
    msg = browser.find_elements_by_tag_name('p')[-1].text
