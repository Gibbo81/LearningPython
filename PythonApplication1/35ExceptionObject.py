import files35.PersonalException as pe
import sys

def raise0():
    raise pe.GeneralException

def raise1():
    raise pe.SpecificException1

def raise2():
    raise pe.SpecificException2





print('---------------------------------------------------------------------')
print('Raise all the exception of the hierarchy')
for x in (raise0, raise1, raise2):
    try:
        x()
    except pe.GeneralException as e:             #catches all the hierarchy of exception classes
        print("caught %s" % sys.exc_info()[0])   #gives information about the most recent exception
                                                 #reaslly usefull with empty except where we cannot use as... 
        print("/*/*/*e.__class__: %s*/*/*/" % e.__class__)
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')
