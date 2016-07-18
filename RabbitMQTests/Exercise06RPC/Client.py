import pika
import uuid

class Fibonacci():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        print("client connection created CCC")
        self.result = self.channel.queue_declare(exclusive=True)     #Declare the callback queue
        self.callback_queue = self.result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True, queue = self.callback_queue)

    def on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.body = body
        
    def RPCCall(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
            
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to = self.callback_queue, 
                                                                   correlation_id = self.corr_id),
                                   body = str(n))
        '''
        We use a default exchange identified by an empty string. 
        This exchange is special: it allows us to specify exactly to which queue the message 
        should go. The queue name needs to be specified in the routing_key parameter:
        '''            
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)
            
if __name__ == '__main__':
    fibonacciRPC =  Fibonacci()
    print("reques fib 30")
    response = fibonacciRPC.RPCCall(30)
    print('Answer is %s' % response)









