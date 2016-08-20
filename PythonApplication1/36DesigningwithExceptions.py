import sys




print('---------------------------------------------------------------------')
print("if no exception has been handele sys.exc_info() return three none")
obj = sys.exc_info()
count = 0
for x in obj:
    print("sys.exc_info()[%s]: %s" % (count, x))
    count+=1
print('---------------------------------------------------------------------')
print('instead if we have a real exception')
try:
    raise BrokenPipeError("error")
except:
    obj  = sys.exc_info()
    count = 0
    for x in obj:
        print("sys.exc_info()[%s]: %s" % (count, x))
        count+=1
print('When we exit the except block the exception has been managed and sys.exc_info() return again three NONE')
obj2 = sys.exc_info()
count = 0
for x in obj2:
    print("sys.exc_info()[%s]: %s" % (count, x))
    count+=1
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')