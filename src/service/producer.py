import tweepy
from dotenv import (
    load_dotenv, find_dotenv)
from datetime import datetime
from json import dumps
from kafka import KafkaProducer

consumer_key = 'sGQILZrjvzZ9an1z7geMkDCd5'
consumer_secret = 'teqBAfvMiEeXgy4sigeSDl5GdA8iLvOg4Y1mT7W7k3XD363K6P'
access_token = '1405683717851467779-s1cBXnJ3rJwvabMxapDUtGwe3yAZsg'
access_token_secret = 'TCTiP3Z3Il6Xr4dmSDafXjuhAQ9yoEfB61Th0yyzoKepV'

broker = 'localhost:9092'
topico = 'scraping-twitter'
producer = KafkaProducer(
    bootstrap_servers=[broker],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
twitts = api.search('Alura')



for i in twitts:
    frase = str(i.text)
    data_e_hora = datetime.now()
    data_string = data_e_hora.strftime('%Y-%m-%d %H:%M:%S')

    data = {
        "tweet": frase,
        "horario": data_string
    }

    producer.send(topico, value=data)

