from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_05.html'
browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_05.html')


sleep(2)
while True:
    sleep(1)
    span = browser.find_element_by_css_selector('span').text
    if span == 'l0c0':
        form = browser.find_element_by_css_selector('[class="form-l0c0"]')
    elif span == 'l0c1':
        form = browser.find_element_by_css_selector('[class="form-l0c1"]')
    elif span == 'l1c0':
        form = browser.find_element_by_css_selector('[class="form-l1c0"]')
    elif span == 'l1c1':
        form = browser.find_element_by_css_selector('[class="form-l1c1"]')
    if '... Mentira, você conseguiu terminar' in span:
        break
    nome = form.find_element_by_css_selector('[type="text"]')
    nome.send_keys('JOSE')
    senha = form.find_element_by_css_selector('[type="password"]')
    senha.send_keys('1643114')
    btn = form.find_element_by_css_selector('[type="submit"]')
    btn.click()