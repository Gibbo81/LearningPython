
def fetch(x, number):
    return x[number]



class MyException(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return ("I'm really a bad exception, %s" % self.text)


print('---------------------------------------------------------------------')
try:
    print(fetch("spam",3))
    print(fetch("spam",4))

except IndexError as e: 
    print("Error raised: %s" % e)

print('continuing')
print('---------------------------------------------------------------------')
try:
    raise IndexError
except IndexError as e: 
    print("Error raised: %s" % e)
print('---------------------------------------------------------------------')
print('User define exception')
try:
    raise MyException("not a great day")
except MyException as e: 
    print("Error raised: %s" % e)
print('---------------------------------------------------------------------')
print('Using try + exception + finally')
try:
    raise MyException("using a finally")
except MyException as e: 
    print("Error raised: %s" % e)
finally:
    print('THIS IS ALWAYS PRINT!!!!')
print('---------------------------------------------------------------------')