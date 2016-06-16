import pika

def callback(ch, method, properties, body):
    print(str(body))
    print('The payload of the message is : %s' % body.decode('UTF-8'))  #you can decode a bytes into a str
#str = '...' literals = a sequence of Unicode characters (UTF-16 or UTF-32, depending on how Python was compiled)
#bytes = b'...' literals = a sequence of octets (integers between 0 and 255)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

channel.queue_declare(queue='hellopython')
channel.basic_consume(callback,queue='hellopython',no_ack=True)

print("Starting consuming messages")
channel.start_consuming()



