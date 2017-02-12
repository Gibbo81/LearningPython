"""
In terms of code, function decorators automatically map the following syntax:
@decorator 
def F(arg):     ==>     F = decorator(F)
This automatic name rebinding works on any def statementn When the function F is later 
called, it's actually calling the object returned by the decorator,
"""
import types

def decorationFunction(F):  
    print('The decorator is created!')      #run after @decorationFunction
    def wrapper(*args):
        print('The decorator is called!')
        print("first parameter: %s" % args[0])
        print("second parameter: %s" % args[1])
        F(*args)                            #Call the original calling function
    return wrapper 

@decorationFunction     #this is run only the first time and crete a link to the correct code
def func(first, second):
    print("Orignal function is called with parameter %s, %s" % (first, second))     

class Decorator:
    def __init__(self, func):
        print('The class decorator is Created!')
        self.func = func
    def wrapper(self, *args):
        print('The class decorator is called!')
        print("first parameter: %s" % args[0])
        print("second parameter: %s" % args[1])
        self.func(*args)  
    def __call__(self, *args):              #we use __call__ to wrap the call
        self.wrapper(args[0],args[1])

@Decorator     #this is a class name
def func2(first, second):
    print("Orignal function 2 is called with parameter %s, %s" % (first, second))    

def decorationFunctionOfAClass(F):  
    print('The decorator is created!')      #run after @decorationFunction
    def wrapper(*args):                     #args[0] is the istance of the class
        print('The decorator is called!')
        print("first parameter: %s" % args[1])
        print("second parameter: %s" % args[2])
        args[0].original()                  #we can use it as a normal instance
        F(*args)                            #Call the original calling function
    return wrapper 

class ToDecorate():
    @decorationFunctionOfAClass 
    def func(self, first, second):
        print("Orignal class function is called with parameter %s, %s" % (first, second))    
    def original(self):
        print('we can still call original istance method')

"""
@decorator 
class C:
...
x = C(99) ==> C = decorator(C)

"""

def eggsfunc(obj):
    return obj.value * 4
def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc # Manages class, not instance
    aClass.ham = hamfunc # Equiv to metaclass __init__
    return aClass

@Extender
class Client1: # Client1 = Extender(Client1)
    def __init__(self, value): # Rebound at end of class stmt
        self.value = value
    def spam(self):
        return self.value * 2


print('---------------------------------------------------------------------')
print('simple decorator using')
func(1,3)
x=func
x(8,9)
print('---------------------------------------------------------------------')
print('simple decorator using class __call__')
func2(7,98)
func2(115,0)
print('---------------------------------------------------------------------')
print('To decorate a class method we MUST use function and not class')
x=ToDecorate()
x.func(54,82)
x.func(439,754)
print('---------------------------------------------------------------------')
print("We can use decorator to add methods to istance after istance creation!")
c=Client1('10')
print('X.spam(): ',c.spam())
print('X.eggs(): ',c.eggs())
print("X.ham('bacon'): ", c.ham('bacon'))
print('---------------------------------------------------------------------')
print("we can use a function to create a class decorator in a dinamic way")
def decoratorf(func):
    def OnCall(*args,**kwargs):
        print('Run the decorators!!!')
        return func(*args,**kwargs)
    return OnCall

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is types.FunctionType:
                setattr(aClass, attr, decorator(attrval)) 
        return aClass       #return the class not an isance
    return DecoDecorate     #return the method not an istance

@decorateAll(decoratorf)     # Use a class decorator, the one returned from method decorateAll(...)
class Person:               # Applies func decorator to methods
    def __init__(self, name, pay): # Person = decorateAll(..)(Person)
        self.name = name            # Person = DecoDecorate(Person)
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

p = Person ("ann", 1000)
print("p.lastName() :", p.lastName())
p.giveRaise (10)
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')