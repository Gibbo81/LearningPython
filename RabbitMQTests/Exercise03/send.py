import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

exchangename='logs'
channel.exchange_declare(exchange=exchangename, type = 'fanout', durable = True)   #fanout -->broadcasts all the messages to all the queues it knows
print("Exchange %s Created" % exchangename)

def BuildMessage(difficulty):
    message=''
    for x in range(0,difficulty):
        message += '.'
    return message

def SendVariableComplexityMessage(difficulty):   
    message = BuildMessage(difficulty)
    result = channel.basic_publish(exchange = 'exchangename',
                                   routing_key = '',
                                   body = message,
                                   properties = pika.BasicProperties(delivery_mode=2)) # make message persistent
    if result:
        print('Send message %s on exchange %s' % (message, exchangename))
    else:
        print("Error")

if __name__ == '__main__':
    SendVariableComplexityMessage(4)
    SendVariableComplexityMessage(5)
    SendVariableComplexityMessage(6)
    SendVariableComplexityMessage(7)
    SendVariableComplexityMessage(8)
    SendVariableComplexityMessage(9)



'''
channel.queue_declare(queue='task_queue', durable=True)

def BuildMessage(difficulty):
    message=''
    for x in range(0,difficulty):
        message += '.'
    return message

def SendVariableComplexityMessage(difficulty):   
    message = BuildMessage(difficulty)
    result = channel.basic_publish(exchange = '',
                                   routing_key = 'task_queue',
                                   body = message,
                                   properties = pika.BasicProperties(delivery_mode=2)) # make message persistent
    if result:
        print('Send message %s on task_queue' % message)
    else:
        print("Error")

if __name__ == '__main__':
    SendVariableComplexityMessage(4)
'''
