import pika, json
from pika import connection
from pika import channel

param = pika.URLParameters()

connection = pika.BlockingConnection(param)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main', body=json.dumps(body), properties=properties)
