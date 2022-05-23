from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_05_b.html'
browser = Firefox()
browser.get(url)

topico = browser.find_element_by_class_name('topico')
linguagens = browser.find_elements_by_class_name('linguagens')

for linguagen in linguagens:
    print(linguagen.find_element_by_tag_name('h2').text)
