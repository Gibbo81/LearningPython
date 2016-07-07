import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print("Connection Created")

exchangename='Tutorial_5_Topic'
channel.exchange_declare(exchange = exchangename, type = 'topic', durable = False)   #topic --> routink key is a list of word *.lazy.orange.#
print("Exchange %s Created" % exchangename)

def BuildMessage(routingKey):
    import random
    message=str(random.randint(1,1010)) + ' ' + routingKey
    return message

def SendVariableComplexityMessage(routingKey):   
    message = BuildMessage(routingKey)
    result = channel.basic_publish(exchange = exchangename,
                                   routing_key = routingKey,
                                   body = message,
                                   properties = pika.BasicProperties(delivery_mode=2)) # make message persistent
    if result:
        print('Send message %s on exchange %s' % (message, exchangename))
    else:
        print("Error")

if __name__ == '__main__':
    SendVariableComplexityMessage("land.rabbit.white")
    SendVariableComplexityMessage("sea.trout.gray")
    SendVariableComplexityMessage("air.hawk.brown")
    SendVariableComplexityMessage("land.fox.white")
    SendVariableComplexityMessage("land.rabbit.red")
    SendVariableComplexityMessage("sea.shark.white")
    SendVariableComplexityMessage("air.canary.yellow")
    channel.close()
    connection.close()
    

