import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

channel.queue_declare(queue='hellopython')
'''
All we need to know now is how to use a default exchange identified by an empty string. 
This exchange is special: it allows us to specify exactly to which queue the message 
should go. The queue name needs to be specified in the routing_key parameter:
'''
result = channel.basic_publish(exchange = '',
                               routing_key = 'hellopython',
                               body = 'Hello World!')
if result:
    print('published message to queue hellopython')
else:
    print("Error")