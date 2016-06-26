import files31.UpperCase as UC
import sys

class BeautifulWriter():
    def write(self, data):
        print("A beautifl writer ",data,end='')

class Wrapper():
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self, name):
        return getattr(self.wrapped,name)

'''
within a class statement only, any names that start with two underscores but don't end with two 
underscores are automatically expanded to include the name of the enclosing class at their front
'''
class ManglingWork():
    def __init__(self, value):
        self.__x = value    ##__X is changed into _classname__x --> _ManglingWork__x
    def __iyi(self):
        print('Mangling work also with method')

class ManglingWorkBis():
    def __init__(self,value):
        self.__x = value    
    def __iyi(self):
        print('Mangling work also with method')

class FinalMangling(ManglingWork, ManglingWorkBis):
    def __init__(self, x1, x2):
        ManglingWork.__init__(self, x1)
        ManglingWorkBis.__init__(self, x2)

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

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')