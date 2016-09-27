"""
In terms of code, function decorators automatically map the following syntax:
@decorator 
def F(arg):     ==>     F = decorator(F)
This automatic name rebinding works on any def statementn When the function F is later 
called, it's actually calling the object returned by the decorator,
"""


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
        args[0].original()                  #we can use it as a normalistance
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