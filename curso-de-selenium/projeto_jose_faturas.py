from selenium.webdriver import Firefox

b = Firefox()
url = ('https://contaonline.claro.com.br/webbow/login/initPJ_oqe.do')
b.get(url)

login = b.find_element_by_css_selector('[type="text"]').send_keys('121644862')
senha = b.find_element_by_css_selector('[type="password"]').send_keys('121212')
btn = b.find_element_by_css_selector('[type="image"]').click()
