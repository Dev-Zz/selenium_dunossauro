import urllib.request, json 
import re
from time import sleep
from selenium.webdriver import Firefox
from datetime import datetime


#Lógica para pegar os dados: LOGIN, SENHA, OPERADORA, CÓDGO DE CLIENTE de cada TICKET.
with urllib.request.urlopen("https://api.movidesk.com/public/v1/tickets?token=1f777488-5e9c-4330-8259-24ab5f6ac50b&id=7041") as url:
    data = json.loads(url.read().decode())
print(data)

#pega a actions [1]
for interacao in data['actions']:
    id = interacao['id']
    if id == 1:
        descricao = interacao['htmlDescription']
print(descricao)

login = re.search('LOGIN:&nbsp;(.*?)<', descricao, flags=re.IGNORECASE)
if login is not None:
    login = login.group(1)
print(login)

senha = re.search('SENHA: (.*?)<', descricao, flags=re.IGNORECASE)
if senha is not None:
    senha = senha.group(1)
print(senha)

operadora = re.search('OPERADORA: (.*?)<', descricao, flags=re.IGNORECASE)
if operadora is not None:
    operadora = operadora.group(1)
print(operadora)

cod_cliente = re.search('CÓDIGO DE CLIENTE:&nbsp;(.*?)<', descricao, flags=re.IGNORECASE)
if cod_cliente is not None:
    cod_cliente = cod_cliente.group(1)
print(cod_cliente)

#Script para abrir o site da TITANIA.
url = 'https://central.titania.com.br/'
browser = Firefox()
browser.get(url)

#clicar em ()CNPJ
sleep(2)
clique_cnpj = browser.find_element_by_css_selector('[value="J"]').click()

#preencher Número do Documento
numero_do_documento = browser.find_element_by_css_selector('[name="login"]').send_keys(login)

#preencher Senha
senha_site_titania = browser.find_element_by_css_selector('[name="password"]').send_keys(senha)

#clicar em logar
logar = browser.find_element_by_css_selector('[name="op"]').click()

#pagina Minha Conta
tbody = browser.find_element_by_css_selector('tbody')
cod_cliente_site_titania = tbody.find_element_by_css_selector('td').text.split()
cod_cliente_site_titania = cod_cliente_site_titania[1]

#logica para pag: Segunda via Boleto
if cod_cliente == cod_cliente_site_titania:
    browser.find_element_by_css_selector('[href="/soucliente/segunda_via"]').click()
else:
    print('CÓDIGOS NÃO BATEM!')

#logica para Download de Fatura, ENCONTRAR O MÊS ATUAL, ENCONTRAR O MÊS NO SISTEMA TITANIA, SEPARAR TODOS OS DADOS PARA PODER COMPARAR.
data_atual = datetime.now()
mes = data_atual.month
tbody = browser.find_element_by_css_selector('tbody')
mes_titania = tbody.find_element_by_css_selector('td')
mes_titania = int(mes_titania.text.split('/')[1].lstrip('0'))

#logica para COMPARAR os dados e fazer download da FATURA.
if mes == mes_titania:
    tbody.find_element_by_css_selector('[value="Gerar Boleto"]').click()
else:
    print('MESÊS NÃO BATEM!!')

#FAZER O DOWNLOAD
cod_boleto = tbody.find_element_by_css_selector('[class="btnboleto form-submit"]')
cod_boleto = cod_boleto.get_attribute('onclick')
cod_boleto = cod_boleto.split()
cod_boleto = cod_boleto[0].strip('geturl_tela').strip('();').strip('')

jsrequest = '''var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://central.titania.com.br/sites/all/files/paginas/getdoc.php', false);
xhr.send('method=boleto&param=AAC60VZ40O&server=integrator_documents');
return xhr.response;'''

result = browser.execute_script(jsrequest)
