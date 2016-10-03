class C: pass

class Eggs:pass
class Spam(Eggs):
    data = 1 
    def meth(self, arg):
        return self.data + arg

class Meta(type):                #meta are normal class that derives from type
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

class MetaWithMetod(type):
        def __new__(meta, classname, supers, classdict):    #called at the and of MetaSpam class statement
            print("Starting MetaWithMetod __new__")
            return type.__new__(meta, classname, supers, classdict)     
        def read(cls):
            return 'read from metaclass MetaWithMetod'   
        def x(cls):
            print('x',cls)  #A is a metaclass itstance are classes (istances=classes)

class Reading(metaclass=MetaWithMetod):
    def Re(self):
        return 'readingoriginal class'

#this metaclass defines a method that as en effect on the class creating istance x
class AT(type):
    def aMeta(cls):
        cls.x = cls.y + cls.z 
    def __getitem__(cls,i):
        return cls.data[i]

class BT(metaclass=AT):
    y,z = 10,21
    data='spamming'
    @classmethod
    def bClass(cls):
        return cls.x
    def __init__(self, one, two):
       self.__class__.y = one               #to change a class variable from an istance
       self.__class__.z = two


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
"""Creation with standard metaclass"""
ms= MetaSpam(4)
ms= MetaSpam(8)

print('---------------------------------------------------------------------')
'''metaclass attributes are made available to their instance classes, but not to instances of 
those instance classes'''
r = Reading()
print('r.Re() :',r.Re())
#print('r.read() :',r.read())   
#this method will raise an error because istance of reading do not take method from MetaWithMetod
print('Reading.Re(r) :',Reading.Re(r))
print('Reading.read() ) :',Reading.read())  #Methods acquired from metaclasses are bound to the subject class

print('---------------------------------------------------------------------')
"""classes acquire metaclass attributes through their __class__ link, in the same way that normal 
instances inherit from classes through their __class__, which makes sense, given that classes are 
also instances of metaclasses"""
class M(type): attr = 1
class A: attr = 2
class B(A): pass
class C(B, metaclass=M): pass 
I = C()
print('I.__class__ :',I.__class__ )
print('C.__bases__ :',C.__bases__)
print('C.__class__ :',C.__class__)
print('C.__class__.attr : ',C.__class__.attr)

print('---------------------------------------------------------------------')
print('To look up an explicit attribute name:')
print('From an instance I, search the instance, then its class, and then all its superclasses')
print('From a class C, search the class, then all its superclasses, and then its metaclasses tree')
print('---------------------------------------------------------------------')
print("DEfine a metaclass that change the class")
ist=BT(100,500)
#ist.aMeta()  #istance cann't see this method, is usable only by the class
BT.aMeta()  #this create attribute x
print('After the creatin of x we can use it from normal istance')
print('ist.x: ',ist.x)
print('BT.x: ',BT.x)
print('ist.bClass(): ', ist.bClass())
print("BT[5]: ",BT[5])
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')