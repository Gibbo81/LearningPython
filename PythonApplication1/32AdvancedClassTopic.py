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

print('------------------------------------------------------------')
