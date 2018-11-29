'''
Projeto para facilitar o acompanhamento do recebimento dos proventos
dos fundos imobiliarios.
As informações são obtidas pelo arquivo html da página.
Ainda não finalizado, pois falta pegar separadamente os fundos.
A intenção é fazer automaticamente (modal.py)
'''

from bs4 import BeautifulSoup
import pandas as pd

caminho_proventos = 'C:\\Users\\ADMIN\\Documents\\Proventos.html'

arquivo_proventos = open(caminho_proventos)

arquivo_excel = open('C:\\Users\\ADMIN\\Documents\\Tabela_Proventos.xls', 'w')

soup = BeautifulSoup(arquivo_proventos, 'html.parser')

tabela = soup.find(class_='table-responsive')

print('Referente ao nome de cada coluna: ')
nome_coluna = soup.select('thead th')
print(nome_coluna)
lista = []
for item in nome_coluna:
    lista.append(item.text)
print()
print('Lista')
for i in range(lista.__len__()):
    print(lista[i])

# Informacoes do dividendo
body = soup.select('tbody tr td')
print(type(body))
print(body[0:8])

lista_pagamento = []
i = 0
while i < body.__len__():
    lista_pagamento.append(body[i].text)
    i = i + 8

lista_papel = []
i = 1
while i < body.__len__():
    lista_papel.append(body[i].text)
    i = i + 8

lista_descricao = []
i = 2
while i < body.__len__():
    lista_descricao.append(body[i].text)
    i = i + 8

lista_tipo = []
i = 3
while i < body.__len__():
    lista_tipo.append(body[i].text)
    i = i + 8

lista_quantidade = []
i = 4
while i < body.__len__():
    lista_quantidade.append(body[i].text)
    i = i + 8

lista_valor_bruto = []
i = 5
while i < body.__len__():
    lista_valor_bruto.append(body[i].text)
    i = i + 8

lista_valor_ir = []
i = 6
while i < body.__len__():
    lista_valor_ir.append(body[i].text)
    i = i + 8

lista_valor_liquido = []
i = 7
while i < body.__len__():
    lista_valor_liquido.append(body[i].text)
    i = i + 8

df_data = {
    'Data_Pagamento': lista_pagamento,
    'Papel': lista_papel,
    'Descrição': lista_descricao,
    'Tipo': lista_tipo,
    'Quantidade': lista_quantidade,
    'Valor Bruto': lista_valor_bruto,
    'Valor IR': lista_valor_ir,
    'Valor Líquido': lista_valor_liquido
}

df_data_reduzido = {
    'Data_Pagamento': lista_pagamento,
    'Papel': lista_papel,
    'Quantidade': lista_quantidade,
    'Valor Líquido': lista_valor_liquido
}

df = pd.DataFrame(df_data)
df_reduzido = pd.DataFrame(df_data_reduzido)
print(df)
arquivo_excel.write(str(df_reduzido))
'''
df_data = {
    'Data_Pagamento':
}
'''