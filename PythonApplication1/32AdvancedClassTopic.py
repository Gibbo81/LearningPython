class SearchingTest:     
    def __init__(self, value):
        self.Data=value
    def __add__(self, other):
        return SearchingTest(self.Data + other)

class Base: attr = 1
class A(Base): pass
class B(Base): attr = 2
class C(A,B): pass

class Base1: pass
class A1(Base): pass
class B1: pass
class C1(A1,B1): pass

class Slot: #It"s possible to force a clas to only have a subset of attribute by defining them into __slot__
    __slots__ = ['age','name','secondname','job']   #class level attribute

#We can still accommodate extra attributes, though, by including __dict__ explicitly in
#__slots__, in order to create an attribute namespace dictionary too:
class SlotAndDict():
    __slots__ = ["A","B","C","__dict__",]
    def __init__(self, x, y):
        self.notinslot = x  #inside __dict__ we wil have only the attribute not in __slot__
        self.A = y
#!!!!!It's the presence of __dict__ that enable us to add dinamically new attribute to the class!!!!!!


class properties():         #Using properties
    def __init__(self):
        self.agep=40

    def getage(self):
        print("Getting age")
        return self.agep
    def setage(self, value):
        print("Setting age, new value %s" % value)
        self.agep = value
    age = property(getage, setage, None, None)

print('------------------------------------------------------------')
a= SearchingTest(10)
#a.__add__= lambda x: self.Data + x     #this is not working 
                                        #we are searching for __add__ inside the class not the istance!!!
b= a+12
print(b.Data)
print('------------------------------------------------------------')
print('Diamond Inheritance tree')
x = C()
print(x.attr)                               #the new search pattern MRO{method resolution order} is: x C A B base
print("The value is taken from B class")    #the old one (2.X) would be x C A Base B
print("Class c new search pattern for diamond --> C.__mro__: ", C.__mro__)
print('------------------------------------------------------------')
#For nondiamonds, though, the search is still as it has always been to the top, and then to the right
print("Class c1 OLD search pattern (NO diamond) --> C1.__mro__: ", C1.__mro__)
print('------------------------------------------------------------')
print("Working with __slot__")
print('It"s possible to force a clas to only have a subset of attribute by defining them into __slot__')
u1 = Slot()
u2 = Slot()
u1.name = "bob"
u2.name = "sillas"
print('u1.__slots__: ',u1.__slots__)
print("u1.name: ",u1.name)
print("u2.name: ",u2.name)
#u.hair = 'red'  #AttributeError: 'Slot' object has no attribute 'hair' 

print('If needed we can include __dict__ explicitly in __slots__,')
sad = SlotAndDict(40,98)
sad.fuffa = 76
print("sad.__dict__: ",sad.__dict__)
print("To see all the attribute")
print("[x for x in dir(sad) if not x.startswith('__')]: " , [x for x in dir(sad) if not x.startswith('__')])
print('------------------------------------------------------------')
print("Working with properties")
p = properties()
print(p.age)
p.age = 65
print(p.age)
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')
