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

query = input('Pesquisa: ')
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

requisicao_decodificada = requisicao[1].decode()  # teve que fazer isso porque se trata de uma tupla

objeto = json.loads(requisicao_decodificada)

tweets = objeto['statuses']

for tweet in tweets:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print()

'''
import pprint
pprint.pprint(objeto['statuses'][0]['user']['screen_name'])
pprint.pprint(objeto['statuses'][0]['text'])
'''