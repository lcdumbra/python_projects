from twitter import Twitter

#Adquiridos pelo twitter
consumer_key = '***'
consumer_secret_key = '***'
access_token = '***'
access_secret_token = '***'

twitter = Twitter(consumer_key, consumer_secret_key, access_token, access_secret_token)

# twitter.post_tweet('Testando o método search')

tweets = twitter.search('dumbra')

for tweet in tweets:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print()