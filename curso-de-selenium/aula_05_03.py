from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_05_c.html'
browser = Firefox()
browser.get(url)

def melhor_filme(browser, filme, email, telefone):
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme(
    browser,
    'Matrix',
    'ejose798@gmail.com',
    '(065)981020200'
)
