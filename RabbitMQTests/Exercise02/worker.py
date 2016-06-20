﻿import pika
import time

def CallBack(ch, method, properties, body):
    print("Start working on message")
    time.sleep(body.decode('UTF-8').count('.'))        #its the same body.count(b'.')
    print('Completed work on message %s' % body.decode('UTF-8')) 

def CreateConsumer(name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Connection Created")

    channel.queue_declare(queue='task_queue')
    channel.basic_consume(CallBack,queue='task_queue',no_ack=True)

    print("Starting consuming messages by %s" % name)
    channel.start_consuming()

if __name__ == '__main__':
    CreateConsumer('Main')