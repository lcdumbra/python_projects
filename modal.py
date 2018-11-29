import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browse = webdriver.Chrome()
browse.get('https://logado.modalmais.com.br/Home/Login')

time.sleep(1)
search_login = browse.find_element_by_name('Login')
search_password = browse.find_element_by_name('Senha')
search_login.send_keys('***') #usuario
search_password.send_keys('***') #senha
button = browse.find_element_by_id('btn-login')
button.click()
browse.implicitly_wait(2)


window_handle_home = browse.get_window_position('current')
botao = browse.find_element_by_id('link-bolsa')
botao.click()

link = browse.find_element_by_link_text('Proventos a Receber')
link.click()

time.sleep(3)

url = browse.current_url
print('Esse é o current_url', url)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_='table-responsive')
print('Imprimindo o que página de proventos')
print(soup.prettify())

'''
url = browse.current_window_handle
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_='table-responsive')
print('Imprimindo o que página de proventos')
print(soup.prettify())

row = soup.select('thead')
rows = (r.get_text() for r in row)
print(rows)
'''

time.sleep(2)

browse.quit()
