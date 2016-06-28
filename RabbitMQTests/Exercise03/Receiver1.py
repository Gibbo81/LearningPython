import pika

def CallBack(ch, method, properties, body):
    print('Completed work on message %s' % body.decode('UTF-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)    #ch --> channel

def CreateConsumer1(exchangename, queuename):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Connection Created")

    channel.queue_declare(queue = queuename, durable = False)
    channel.queue_bind(exchange = exchangename, queue = queuename)
    print('Queue %s created and binded' % queuename)

    channel.basic_qos(prefetch_count=2)                 #take only two message at the time
    channel.basic_consume(CallBack,queue = queuename)

    print("Starting consuming messages by %s" % queuename)
    channel.start_consuming()


if __name__ == '__main__':
    import random
    queuename = "QConsumer" + str(random.randint(1,1010))
    CreateConsumer1('logs', queuename)





