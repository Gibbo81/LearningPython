
def fetch(x, number):
    return x[number]



class MyException(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return ("I'm really a bad exception, %s" % self.text)


class Student():
    def __init__(self,x):
        self.x = x

print('---------------------------------------------------------------------')
try:
    print(fetch("spam",3))
    print(fetch("spam",4))

except IndexError as e: 
    print("Error raised: %s" % e)

print('continuing')
print('---------------------------------------------------------------------')
try:
    raise IndexError("Manually raised")
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
print('--------------------------------------------------------------------')
print("methods can always be assigned to a class after it's been created, as long as the methods assigned are functions with an extra first argument to receive the subject self instance")

def sum(obj, value):
    return obj.x + value

s=Student(100)
Student.sum=sum

print("s.sum(88): %s" % s.sum(88))

print("we have to repeat the augmentation code for every class that needs these methods")
print('Or we can add to a super class and simple use inheritance')
print('---------------------------------------------------------------------')