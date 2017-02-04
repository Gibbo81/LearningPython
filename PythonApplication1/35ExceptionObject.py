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
    except pe.GeneralException as e:                    #catches all the hierarchy of exception classes
        print("caught type exception %s" % sys.exc_info()[0])   #gives information about the most recent exception (its type)
        print("Exception instance: %s" % sys.exc_info()[1])     #give the real exception instance
        print("/*/*/*e.__class__: %s*/*/*/" % e.__class__)#really usefull with empty except where we cannot use as... 
        print('+++++++++++++++++++++++++++++++++++++++++++++++')
print('---------------------------------------------------------------------')
print("Default printing and state")
ex = TimeoutError(1,2,3,'a','b','c')
print("TimeoutError(1,2,3,'a','b','c').args: %s" % str(ex.args))
print("TimeoutError(1,2,3,'a','b','c'): %s" % ex)
'''
Unless you redefine the constructors your exception classes inherit from the superclass, any constructor 
arguments you pass to these classes are automatically saved in the instance's args tuple attribute, and 
are automatically displayed when the instance is printed
'''
print('---------------------------------------------------------------------')
print('It works also for personalized exception (no override)')
ex = pe.SpecificException2(1,2,3,'a','b','c')
print("pe.SpecificException2(1,2,3,'a','b','c').args: %s" % str(ex.args))
print("pe.SpecificException2(1,2,3,'a','b','c'): %s" % ex)
print('---------------------------------------------------------------------')