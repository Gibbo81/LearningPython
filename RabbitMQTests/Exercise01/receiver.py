import pika

def callback(ch, method, properties, body):
    print(str(body))
    print('The payload of the message is : %s' % str(body))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

channel.queue_declare(queue='hellopython')
channel.basic_consume(callback,queue='hellopython',no_ack=True)

print("Starting consuming messages")
channel.start_consuming()



