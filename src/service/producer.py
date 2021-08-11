import tweepy
import os
from dotenv import (
    load_dotenv, find_dotenv)
from datetime import datetime
from json import dumps
from kafka import KafkaProducer

load_dotenv(find_dotenv())

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

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

