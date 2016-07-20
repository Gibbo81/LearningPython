import pika
import time

def Consume(ch, method, properties, body):
    print("Start working on %s" % body.decode('UTF-8'))
    time.sleep(body.decode('UTF-8').count('.')) 
    print("Complete working on %s" % body.decode('UTF-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1) 
    print("Connection Created")
    channel.basic_consume(Consume, queue = "ManualTest")

    count=0
    while count<2:                              #we want to elaborate only 2 messages {prefetch_count=1}
        count = count +1
        connection.process_data_events()        #Read all the messages but it's not stopping. Onme time event!!!!
    print("completed elaboration of %s messages" % count)
    channel.close()
    connection.close()
