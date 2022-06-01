'''Pegar todos os dados da PAGINA e mostrar para o usuario.

como resolver?

1 - Usar o .find_element_by_css_selector() para encontrar todos os dados.
2 - Entender como colocar isso dentro de uma variavel
3 - Mostrar isso na tela'''


from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(2)

h1 = browser.find_element_by_css_selector('h1').text
ps = browser.find_elements_by_css_selector('p')
dicionario = {}

for p in ps:
    dicionario.update({p.get_attribute('atributo'): p.text})
print('''{}, {}'''.format(h1, dicionario))