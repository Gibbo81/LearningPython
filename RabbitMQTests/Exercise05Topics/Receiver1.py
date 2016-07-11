import pika

def CallBack(ch, method, properties, body):
    print('Completed work on message %s' % body.decode('UTF-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)    #ch --> channel

def CreateConsumer(exchangename, queuename, *routingkey):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=2)                 #take only two message at the time
    print("Connection Created")

    channel.queue_declare(queue = queuename, durable = False)
    for binding_key in routingkey:
        channel.queue_bind(exchange = exchangename, queue = queuename, routing_key = binding_key)
    print('Queue %s created and binded to exchange %s' % (queuename, exchangename))
    
    channel.basic_consume(CallBack, queue = queuename)
    channel.start_consuming()
    print("Starting consuming messages by %s" % queuename)


if __name__ == '__main__':
    import random
    queuename = "QConsumer" + str(random.randint(1,1010))
    CreateConsumer('Tutorial_5_Topic', queuename, "land.#")





