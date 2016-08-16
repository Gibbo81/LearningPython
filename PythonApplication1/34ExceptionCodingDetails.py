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
print("__cause__ is the equivalent of C# inner exception")
try:
    try:
        raise UnboundLocalError("AAA")
    except Exception as e:
        print("Catch Exception")
        raise PermissionError('BBB')  from e        #this  goes inside __cause__ field 
except Exception as e:
    print('External exception: %s' % e)
    print('Internal exception __cause__: %s' % e.__cause__)

print("Its' possible, but not so usefull to create both the exceptions at the same time")
try:
    raise UnboundLocalError("DDD") from AssertionError('CCC')
except Exception as e:
    print('External exception: %s' % e)
    print('Internal exception __cause__: %s' % e.__cause__)
print('---------------------------------------------------------------------')
print('Assert: assert test, data')
print('if the test evaluates to false, Python raises an exception: the data item ')
try:
    r=random.randint(1,100)
    assert (r%2)!=0, "%s it's even" % r
except Exception as e:
    print(e)
    print(e.__class__)      #raise use AssertionError class
#assert statements are removed from a compiled program's byte code if the -O Python command-line flag is used
print('---------------------------------------------------------------------')
print("With an alternative to try/finally")
print("it allows a richer object-based protocol for specifying ENTRY and EXIT actions!")
with open(r'.\\09files\\myfile.txt') as myfile:
    for line in myfile:
        print(line, end='')
print('At the end of the with the file is automatically closed')
print('---------------------------------------------------------------------')
print('We can use with command with more than one expression at the same time')
with open(r'.\\09files\\myfile.txt') as myfile1, open(r'.\\09files\\insertobjects.txt') as myfile2:
    for line in myfile1:
        print(line, end='')
    for line in myfile2:
        print(line, end='')
print('---------------------------------------------------------------------')