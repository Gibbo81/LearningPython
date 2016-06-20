import send
import worker


for x in range(1,19):
    send.SendVariableComplexityMessage(x)
'''
for x in range(1,3):
    name="consumer"+str(x)
    worker.CreateConsumer(name)
'''


