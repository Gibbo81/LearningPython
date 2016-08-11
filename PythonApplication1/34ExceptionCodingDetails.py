import random
  #  print('random.random() :' + str(random.random()))




print('---------------------------------------------------------------------')
try:
    i=random.randint(1,100)
    if ((i%2)==0):
        raise AssertionError
except (RecursionError, AssertionError) as e:
    print("we can check two variable at the same time!")
except:
    print("all the exception types")
else:
    print('we have no exception')

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

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')