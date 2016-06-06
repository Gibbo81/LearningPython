'''
inheritance searches occur only on attribute references, not on assignment: assigning to 
an object’s attribute always changes that object, and no other
'''

class NextClass():
    def printer(self, text):
        self.message=text
        print(text)

class TextMulti__init__():
    def __init__(self, valA, valB):     #this cannot be use
        self.a=valA
        self.b=valB
        print('First costructor')

    def __init__(self, valA):           #this 2° constructor will hide the first one no xostructor overload
        self.a=valA
        print('Second costructor')

class AbstractClass():      #Abstract class expects part of its behavor to be implemented
    def delegate(self):     #inside a derivate class
        self.work()
    def work(self):
        raise NotImplementedError('Action must be defined in a subclass')
        #it's possible to use metadata to tell python that a class is abstract and that can not be istanciated
class ConcreteDerivate(AbstractClass):
    def work(self):
        print("this is the concrete implementation!")

g=1
def nester():
    g=2
    class Inside:
        g=3
        print(g);           #3
        def nested(self):
            print(g)    #2! The lookup rules for simple names like X never search enclosing class
                        #statements—just defs, modules, and built-ins (it’s the LEGB rule, not CLEGB!).
            print(self.g)   #3 To read 3 i have to use self.g
    Inside().nested()   


         
print('--------------------------------------------------------------')
x1=NextClass()
x1.printer('APPO')
#this two are absolutely the same!
x2=NextClass()
NextClass.printer(x2,"APPO")
print('**************************************************************')    
T=TextMulti__init__('p')
#T2=TextMulti__init__('p','z')      this will give back an error

print('--------------------------------------------------------------')
print('ABSTRACT CLASS')
x=ConcreteDerivate()
x.work();
#AbstractClass().work() this would give a run time error
print('**************************************************************')
print('Testing particular scope work')
nester()

print('--------------------------------------------------------------')

print('**************************************************************')
    
print('--------------------------------------------------------------')

print('**************************************************************')
    
print('--------------------------------------------------------------')

print('**************************************************************')