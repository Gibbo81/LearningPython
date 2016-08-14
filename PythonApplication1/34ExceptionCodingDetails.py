import random


print('---------------------------------------------------------------------')
print("try -> except -> else -> finally this is the correct order")
try:
    i=random.randint(1,100)
    if ((i%2)==0):
        raise AssertionError
except (RecursionError, AssertionError) as e:
    print("we can check two variable at the same time!")
except:
    print("all the exception types")
else:
    print('Executed only when we have no exception')
finally:
    print('We can have all this block toghether')

print('---------------------------------------------------------------------')
print("except: Exception")
try:
    i=random.randint(1,100)
    if ((i%2)==0):
        raise SystemExit
    if ((i%3)==0):
        raise UnboundLocalError
except Exception:       #catch all the exception with the esclusion of those related to system exit
    print("catch all the exception with the esclusion of those related to system exit")
except SystemExit:
    print('Catch system exit')
print('---------------------------------------------------------------------')
print("A single try/finnally block does not stop exception")
try:
    try:
        raise UnboundLocalError
    finally:
        print("Finally doesn't block the exception, if there isn't an except block the it goes up on the stack")
except:
    print("all the exception types")
print('---------------------------------------------------------------------')
print('to re-raise  an exception')
print("Usefull to re throw an exception after a catch")
try:
    try:
        raise UnboundLocalError
    except:
        print("Catch UnboundLocalError for the first time")
        raise                   #re-raise the last reised exception
except:
    print("Catch UnboundLocalError for the second time")







print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')