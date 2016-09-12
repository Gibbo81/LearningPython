class Person: 
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "Property docs")  

class BasketPlayer(Person): 
    def getName(self):
        print('fetch Basket Player...')
        return self._name
    name2 = property(getName, Person.setName, Person.delName, "Property docs")  

class PropertyWithDecorator:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):             #this define the property and initialize the get method
        print('fetch...')
        return self._name
    @name.setter                #define the set
    def name(self, value):
        print('change from %s to %s' % (self.name, value))
        self._name = value
    @name.deleter               #define the delete
    def name(self): 
        print('remove...')
        del self._name

class Descriptor:
    "name descriptor docs"                  #this is the property doc
    def __get__(self, instance, owner):     #owner is the type(class) of instance
        print(self, instance, owner, sep='\n')
        return instance.value
    def __set__(self, instance, value):
        print('change from %s to %s' % (instance.value, value))
        instance.value = value  
    def __delete__(self, instance):
        print('remove value ...')
        del instance.value

class Base():
    def __init__(self, value):
        self.value = value
    attr = Descriptor()     #It's a class attribute but instance are automaically passed with each call
  
"""
Also note that when a descriptor class is not useful outside the client class, it's 
possible to embed the descriptor's definition inside its client syntactically (pag.1231)
"""

class CatchAllUndefined():
    def __init__(self, name):
        self.name = name
    def __getattr__(selv, attrname):            #catch all undefine attribute (all autside name)
        return "Attribute %s it's not define" % attrname


print('---------------------------------------------------------------------')
print("Using propertie to access data inside class")
p = Person('Jack')
print(Person.name.__doc__)
print(p.name)
p.name="Aldo"
print(p.name)
del p.name
#print(p.name)                                  # This would give back an error
print('---------------------------------------------------------------------')
print('Properties are inherited by both instance and lower subclasses')
p = BasketPlayer('Jordan')
print(BasketPlayer.name.__doc__)
print(p.name)                                   # we can use both the old and the new one
print(p.name2)
p.name="Mayers"
print(p.name)
print(p.name2)

print('---------------------------------------------------------------------')
'''
Recall that the function decorator syntax:
@decorator
def func(args): ...
is automatically translated to rebind the function name to the result of the decorator callable:
def func(args): ...
func = decorator(func)
'''
print("we can create the same class effect using the decorator @property")
x=PropertyWithDecorator('Norma')
print(x.name)                                  
x.name="Minnis"
print(x.name)
del x.name
#print(x.name)                # This would give back an error
print('---------------------------------------------------------------------')
print("Working with Description")
print(Descriptor.__doc__)
b= Base('Sonya')
print(b.attr)
b.attr="Blade"
print(b.attr)
del b.attr
print('---------------------------------------------------------------------')
print('Working with __getattr__')
c=CatchAllUndefined('Qua')
print(c.name)       #all except this are catch by __getattr__
print(c.surname)
print(c.age)


print('---------------------------------------------------------------------')
'''
getattr function is used to fetch an attribute from an object, using a string object instead of an 
identifier to identify the attribute. In other words, the following two statements are equivalent:

value = obj.attribute
value = getattr(obj, "attribute")
'''
p = Person('Camilla')
print(getattr(p, "_name"),"are the same", p._name)

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')