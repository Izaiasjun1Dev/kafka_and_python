import json
from kafka import KafkaConsumer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from IPython.display import clear_output


broker = ['localhost:9092']
topic = 'scraping-twitter'
consumer = KafkaConsumer(
    topic,
    group_id='group1',
    bootstrap_servers = broker
)

frase = ''
list_twitter = []

for message in consumer:
    texto = json.loads(message.value.decode('utf-8'))
    frases = frase + texto['tweet']
    list_twitter.append(frases)
    print(list_twitter)

    