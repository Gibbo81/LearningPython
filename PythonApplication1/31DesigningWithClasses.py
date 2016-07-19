import files31.UpperCase as UC
import sys

class BeautifulWriter():
    def write(self, data):
        print("A beautifl writer: ", data, end='')
    def writeselfless(data):
        print("A beautifl selfless writer: %s" % data, end='')

class Wrapper():
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self, name):
        return getattr(self.wrapped, name)

'''
within a class statement only, any names that start with two underscores but don't end with two 
underscores are automatically expanded to include the name of the enclosing class at their front
'''
class ManglingWork():       #pseudo private attribute!
    def __init__(self, value):
        self.__x = value    ##__X is changed into _classname__x --> _ManglingWork__x
    def __iyi(self):
        print('Mangling work also with method')

class ManglingWorkBis():
    def __init__(self, value):
        self.__x = value    
    def __iyi(self):
        print('Mangling work also with method')

class FinalMangling(ManglingWork, ManglingWorkBis):
    def __init__(self, x1, x2):
        ManglingWork.__init__(self, x1)
        ManglingWorkBis.__init__(self, x2)

class Without():
    def Selfless(a, b):         #self is not necessary in 3.X we can omit it 
        return a+b

def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)

class Spam():
    def doit(self, message):
        print(message)
class Person():
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

class ReadAllIstanceAttribute():
    def ReadIstanceAttribute(self):
        return list(self.__dict__.items())   #this will find only the attribute of the istance
    def __str__(self):
        return ("This are all the attibutes of a %s: %s" % (self.__class__.__name__, 
                                                            self.ReadIstanceAttribute()))

class ReadAllAttribute():
    def ReadAttribute(self):
        return list(dir(self))              #we can read all the attribu include that of class and inheritance
    def Print(self):
        result=''
        for x in self.ReadAttribute():
            if x[:2]!='__':
                result += "%s : %s\n" % (x, getattr(self,x)) 
        print("Full attribute list: %s " % result)

class p():
    def __init__(self):
        self.nina = 'nina'

    def PWalk(self):
        print("P walking")

class Man(ReadAllIstanceAttribute,ReadAllAttribute, p):
    def __init__(self, name, age):
        p.__init__(self)
        self.name = name
        self.age = age
    
    def ManWalk(self):
        print("Man walking")

print('------------------------------------------------------------')
worker = UC.UpperCase(open('.\\files31\\Righe.txt',"r"), sys.stdout)
worker.process()
print()
worker = UC.UpperCase(open('.\\files31\\Righe.txt',"r"), BeautifulWriter())
worker.process()
print()
print('------------------------------------------------------------')
print('Working with wrapper object -- dinamic access to wrapped attributes')
w1 = Wrapper([1,3,6,8,54])
w1.append(2)
print("position of 2: ", w1.index(2))
print(w1.wrapped)

w2 = Wrapper({'a':2,'y':5})
print(list(w2.keys()))
print(list(w2.values()))
print("It's more or less a kind of run time delegation made with simil reflection")
print('------------------------------------------------------------')
print('Working with Mangling Name!!!!')
"""
Python programmers code internal names with a single underscore (e.g., _X), which is just an 
informal convention to let you know that a name shouldn't generally be changed
"""
m= ManglingWork(50)
print(m._ManglingWork__x)       #__X is changed into _classname__x --> _ManglingWork__x
m._ManglingWork__iyi()          #same for method
print(m.__dict__)
print(ManglingWork.__dict__)
print('------------------------------------------------------------')
print('How Mangling works with inheritance: we will have 2 .x !!!!!!')
mf= FinalMangling(32, "xtwo")
print(mf.__dict__)
print('------------------------------------------------------------')
print("Bound method object")
"""
Accessing a function attribute of a class by qualifying an instance returns a bound method object. 
Python automatically packages the instance with the function in the bound method object, so you 
don't need to pass an instance to call the method.
"""
istance = BeautifulWriter()
object = istance.write          #we can fetch a bound method without actuallly calling it
print(object)
object("messaggio\n")
print("Unbound method object")
'''
Accessing a function attribute of a class by qualifying the class returns an unbound method object. 
To call the method, you must provide an instance object explicitly as the first argument.
'''
object = BeautifulWriter.write  #unbound method to use it we still need an istance
print(object)
object(istance, "messaggio\n")
'''
If the function do not require a self istance def writeselfless(data):
we can call it without passing an istance {NO SELF}
'''
objectselfless = BeautifulWriter.writeselfless
objectselfless("messaggio\n")
print('------------------------------------------------------------')
w = Without()
print(Without.Selfless(24,69))
#print(w.Selfless(10,58))    #Selfless() takes 2 positional arguments but 3 were given. Self is automaticaly passed :-)
print('------------------------------------------------------------')
print('Using a factory')
objs=factory(Spam)
objp1= factory(Person, 'Nick','Driver')
objp2= factory(Person, 'Merlin')
print(objs, objp1, objp2)
print('------------------------------------------------------------')
print("Working with mix-in: multi inheritance")
m= Man("Mario", 45)
print(m)
m.Print()
print('------------------------------------------------------------')