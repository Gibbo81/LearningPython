if __name__ == '__main__':
    import random
    import Receiver1
    queuename = "QConsumer" + str(random.randint(1,1010))
    Receiver1.CreateConsumer('Tutorial_5_Topic', queuename, 'land.*.white')