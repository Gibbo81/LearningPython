import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            ),
                      body=request)
'''
We use a default exchange identified by an empty string. 
This exchange is special: it allows us to specify exactly to which queue the message 
should go. The queue name needs to be specified in the routing_key parameter:
'''