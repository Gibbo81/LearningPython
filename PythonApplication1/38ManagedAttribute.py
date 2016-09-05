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


    #@property
    #def Name(self):
    #    return self.name


print('---------------------------------------------------------------------')
print("Using propertie to acess data inside class")
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
is automatically translated to this equivalent by Python, to rebind the function name
to the result of the decorator callable:
def func(args): ...
func = decorator(func)
'''


print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')