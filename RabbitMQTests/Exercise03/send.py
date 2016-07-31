import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

exchangename='logs'
channel.exchange_declare(exchange = exchangename, type = 'fanout', durable = True)   #fanout -->broadcasts all the messages to all the queues it knows
print("Exchange %s Created" % exchangename)

def BuildMessage(maxmaxDifficulty):
    import random
    message=str(random.randint(1,1010))
    for x in range(0,maxmaxDifficulty):
        message += '.'
    return message

def SendVariableComplexityMessage(maxmaxDifficulty):   
    message = BuildMessage(maxmaxDifficulty)
    result = channel.basic_publish(exchange = exchangename,
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
    connection.close()

