class C: pass

class Eggs:pass
class Spam(Eggs):
    data = 1 
    def meth(self, arg):
        return self.data + arg

class Meta(type):                #meta are normal class that derives from tipe
    def __new__(meta, classname, supers, classdict):    #called at the and of MetaSpam class statement
        print("Starting metaclass __new__")
        return type.__new__(meta, classname, supers, classdict)        
    def __init__(meta, classname, supers, classdict):
        print("Starting metaclass __init__")
        type.__init__(meta, classname, supers, classdict)   
        print("Stopping metaclass __init__")  
'''
notice how the metaclass is invoked at the end of the class statement, before we ever make an 
instance, metaclasses are for processing classes, and classes are for processing normal instances
'''

class MetaSpam(Eggs, metaclass=Meta):   #this time we define a different metaclass to use to build istance
    data = 1 
    def __init__(self, var):
        self.var=var
    def meth(self, arg):
        return self.data + arg


print('---------------------------------------------------------------------')
'''
classes are instances of the type class, just as normal instances are instances of a user-defined 
class. This works the same for both built-ins and user-defined class types. In fact, classes 
are not really a separate concept at all: they are simply user-defined types, and type itself 
is defined by a class.
'''
print("Instances are created from classes, and classes are created from type.")
x = C()
print(type(x))
print(x.__class__)
print(type(C))
print(C.__class__)
print('---------------------------------------------------------------------')
"""
type is a class that generates user-defined classes
To control the way classes are created and augment their behavior, all we need to do is specify that a
user-defined class be created from a user-defined metaclass instead of the normal type class
"""
print("we can create a class calling type in a direct way")
a = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})    #--> a = Spam() +/-
print(a.data)
print(a.meth(a,9))      #a.meth(45) wouldn't working
print('---------------------------------------------------------------------')
ms= MetaSpam(4)
ms= MetaSpam(8)

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