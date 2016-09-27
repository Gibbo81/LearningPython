class C: pass







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

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')