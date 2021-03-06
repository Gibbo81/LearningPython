﻿import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")
channel.queue_declare(queue = 'rpc_queue', durable=True)
print("Created queue rpc_queue")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def on_request(ch, method, properties, body):
    n = int(body)
    print("received request for fibonacci of %s" % n)

    result= fib(n)
    channel.basic_publish(exchange = '',
                          routing_key = properties.reply_to,
                          properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                          body=str(result))

    ch.basic_ack(delivery_tag = method.delivery_tag) 

if __name__ == '__main__':
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')

    print("Awaiting RPC requests")
    channel.start_consuming()

