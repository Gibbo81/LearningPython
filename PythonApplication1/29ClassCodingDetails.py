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

print('**************************************************************')
    
print('--------------------------------------------------------------')

print('**************************************************************')
    
print('--------------------------------------------------------------')

print('**************************************************************')
    
print('--------------------------------------------------------------')

print('**************************************************************')