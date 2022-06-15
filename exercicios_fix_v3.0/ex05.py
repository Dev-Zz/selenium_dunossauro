from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl


url = 'https://selenium.dunossauro.live/exercicio_05.html'
browser = Firefox()
browser.get(url)

#Função para preencher os Inputs.


def encontre_span():
    if s == 'l0c0':
        form = browser.find_element_by_css_selector('[class="form-l0c0"]')
        form.find_element_by_css_selector('[type="text"]').send_keys('Jose')
        form.find_element_by_css_selector('[type="password"]').send_keys('1643114')
        form.find_element_by_css_selector('[type="submit"]').click()
    elif s == 'l0c1':
        form = browser.find_element_by_css_selector('[class="form-l0c1"]')
        form.find_element_by_css_selector('[type="text"]').send_keys('Jose')
        form.find_element_by_css_selector('[type="password"]').send_keys('1643114')
        form.find_element_by_css_selector('[type="submit"]').click()
    elif s == 'l1c0':
        form = browser.find_element_by_css_selector('[class="form-l1c0"]')
        form.find_element_by_css_selector('[type="text"]').send_keys('Jose')
        form.find_element_by_css_selector('[type="password"]').send_keys('1643114')
        form.find_element_by_css_selector('[type="submit"]').click()
    elif s == 'l1c1':
        form = browser.find_element_by_css_selector('[class="form-l1c1"]')
        form.find_element_by_css_selector('[type="text"]').send_keys('Jose')
        form.find_element_by_css_selector('[type="password"]').send_keys('1643114')
        form.find_element_by_css_selector('[type="submit"]').click()

#pag1
sleep(2)

while True:
    sleep(0.5)
    s = browser.find_element_by_css_selector('span').text
    encontre_span()
    print(s)
    if 'Mentira' in s:
        break





