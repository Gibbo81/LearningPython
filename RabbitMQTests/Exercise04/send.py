import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

exchangename='Tutorial_4'
channel.exchange_declare(exchange = exchangename, type = 'direct', durable = True)   #fanout --> binding key exactly match
print("Exchange %s Created" % exchangename)

def BuildMessage(maxmaxDifficulty, routingKey):
    import random
    message=str(random.randint(1,1010)) + routingKey
    for x in range(0,maxmaxDifficulty):
        message += '.'
    return message

def SendVariableComplexityMessage(maxmaxDifficulty, routingKey):   
    message = BuildMessage(maxmaxDifficulty, routingKey)
    result = channel.basic_publish(exchange = exchangename,
                                   routing_key = routingKey,
                                   body = message,
                                   properties = pika.BasicProperties(delivery_mode=2)) # make message persistent
    if result:
        print('Send message %s on exchange %s' % (message, exchangename))
    else:
        print("Error")

if __name__ == '__main__':
    SendVariableComplexityMessage(4,"Blue")
    SendVariableComplexityMessage(5,"Red")
    SendVariableComplexityMessage(6,"Green")
    SendVariableComplexityMessage(7,"Blue")
    SendVariableComplexityMessage(8,"Red")
    SendVariableComplexityMessage(9,"Blue")
    SendVariableComplexityMessage(10,"Green")
    connection.close()

