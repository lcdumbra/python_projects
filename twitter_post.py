import oauth2
import json
import urllib.parse

#Adquiridos pelo twitter
consumer_key = '***'
consumer_secret_key = '***'
access_token = '***'
access_secret_token = '***'

consumer = oauth2.Consumer(consumer_key, consumer_secret_key)  # login
token = oauth2.Token(access_token, access_secret_token)  # senha
cliente = oauth2.Client(consumer, token)  # uniao de login e senha, ou seja, o cliente

query = input('Novo Tweet: ')
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

requisicao_decodificada = requisicao[1].decode()  # teve que fazer isso porque se trata de uma tupla

objeto = json.loads(requisicao_decodificada)

print(objeto)