import files31.UpperCase as UC
import sys

class BeautifulWriter():
    def write(self, data):
        print("A beautifl writer ",data,end='')

class Wrapper():
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self, name):
        return getattr(self.wrapped,name)#self.wrapped.getattr(name) 

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

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')