from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse, parse_qsl
#-----------------------------------------------------------------------#
url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Firefox()
browser.get(url)
sleep(2)
#-----------------------------------------------------------------------#

nome = browser.find_element_by_css_selector(
'[name="nome"]').send_keys('Eduardo'
)

email = browser.find_element_by_css_selector(
'[name="email"]').send_keys('ejose798@gmail.com'
)

senha = browser.find_element_by_css_selector(
'[name="senha"]').send_keys('1643114#Ze'
)

telefone = browser.find_element_by_css_selector(
'[name="telefone"]').send_keys('65981020200'
)

btn = browser.find_element_by_css_selector('[name="btn"]').click()

#-----------------------------------------------------------------------#
sleep(2)
dict_textarea = eval(browser.find_element_by_css_selector('textarea').text)
dict_text_url = dict(parse_qsl(urlparse(browser.current_url).query))
dict_text_url.pop('btn')
assert dict_textarea == dict_text_url
