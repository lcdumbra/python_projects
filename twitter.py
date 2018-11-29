import oauth2
import urllib.parse
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret_key, access_token, access_secret_token):
        self.conexao(consumer_key, consumer_secret_key, access_token, access_secret_token)


    def conexao(self, consumer_key, consumer_secret_key, access_token, access_secret_token):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret_key)  # login
        self.token = oauth2.Token(access_token, access_secret_token)  # senha
        self.cliente = oauth2.Client(self.consumer, self.token)  # uniao de login e senha, ou seja, o cliente

    def post_tweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                                     method='POST')
        requisicao_decodificada = requisicao[1].decode()  # teve que fazer isso porque se trata de uma tupla
        objeto = json.loads(requisicao_decodificada)
        return objeto

    def search(self, query):
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')
        requisicao_decodificada = requisicao[1].decode()  # teve que fazer isso porque se trata de uma tupla
        search_objeto = json.loads(requisicao_decodificada)
        tweets = search_objeto['statuses']
        return tweets