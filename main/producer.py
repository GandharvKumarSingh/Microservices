import pika, json
from pika import connection
from pika import channel

param = pika.URLParameters('amqps://shdbbbdo:aW4v9DxoSwBP0AHcPKp9ztNgS4D0nwfq@puffin.rmq2.cloudamqp.com/shdbbbdo')

connection = pika.BlockingConnection(param)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    print("@@@@@@-------------PUBLISH------------@@@@@@@@@")
    channel.basic_publish(exchange='',routing_key='admin', body=json.dumps(body), properties=properties)