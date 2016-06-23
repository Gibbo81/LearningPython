import pika
import time

def CallBack(ch, method, properties, body):
    print("Start working on message")
    time.sleep(body.decode('UTF-8').count('.'))         #its the same body.count(b'.')
    print('Completed work on message %s' % body.decode('UTF-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)    #ch --> channel

def CreateConsumer(name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Connection Created")

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_qos(prefetch_count=2)                 #take only two message at the time
    channel.basic_consume(CallBack,queue='task_queue')

    print("Starting consuming messages by %s" % name)
    channel.start_consuming()

if __name__ == '__main__':
    CreateConsumer('Main')