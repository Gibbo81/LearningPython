class FirstClass:
    MutableField=[1,2,3]                #this is an attribute present in all the istance
    # change in place will affect all the istance but immutable change or new assignment will create a new local variable for istance, the global one is unaffected  
    #Placeorder AAAAAA
    def SetData(self, value):
        self.Data=value         #this is an attribute is created only in the current running istance
    def PrintData(self):
        print(self.Data)

class SecondClass(FirstClass):          #inheritance
    def PrintData(self):
        print("------OVERLOAD------")
        print('Overloaded method %s :-) :-)' % self.Data)

class OverloadPythonOperators:      #overload 2 operator: tostring and +
    def __init__(self, value):
        self.Data=value
    def __add__(self, other):
        return OverloadPythonOperators(self.Data + other.Data)
    def __str__(self):
        return str('[This class: %s]' % self.Data)

class TestDataPosition:    #Placeorder AAAAAA
    globale = "all"
    def __init__(self, value):
        self.data=value



print(FirstClass.__dict__)
HookNameList= [name for name in FirstClass.__dict__ if name.startswith('__')]
print(HookNameList) 
print('-----------------------------------------------------------------')
istance = FirstClass()
print('Class start out as an emty namespace instance.__dict__: ',istance.__dict__)   #this give out only the attribute of this istance
istance.SetData("testing")
print('But we can create new attribute in the instance ',istance.__dict__)
istance.PrintData()

print('-----------------------------------------------------------------')
istance2 = FirstClass()
istance.MutableField[1]="TTTT"  #In place change will affect all the different istance
print(istance.MutableField)
print(istance2.MutableField)
istance.MutableField=34         #not in place we have created a new local variable for istance, the global one is uneffected
print('Have created a new local instance: ',istance.__dict__)
print(istance.MutableField)
print(istance2.MutableField)
print('-----------------------------------------------------------------')
print('Working with inerithance')
istance3 = SecondClass()
istance3.SetData("Second is better")
istance.PrintData()
istance3.PrintData()
print('-----------------------------------------------------------------')
print("Using overloaded operator")
x1=OverloadPythonOperators("base ")
x2=OverloadPythonOperators("avanzato")
print(x1+x2)                    #uses both + and tostring
print('-----------------------------------------------------------------')
#Placeorder AAAAAA
print("Let's check where pyton put the different operator")     #REALLY IMPORTANT
u1=TestDataPosition('First')
u2=TestDataPosition('Second')
print('class TestDataPosition defined parameter: ',[name for name in TestDataPosition.__dict__ if not name.startswith('__')])
print("List of __dict__ of the first instance: ", list(u1.__dict__.keys()))
print("List of __dict__ of the second instance: ", list(u2.__dict__.keys()))
u1.globale="new global"
print("With u1.globale='new global' I have not changed the global value but defined a new attribute for istance u1")
TestDataPosition.globale="to change all"    #to change the global one i need to do this!
print("List of __dict__ of the first instance: ", list(u1.__dict__.keys()))
print("List of __dict__ of the second instance: ", list(u2.__dict__.keys()))
#The main point to take away from this look under the hood is that Python’s class model
#is extremely dynamic. Classes and instances are just namespace objects, with attributes
#created on the fly by assignment. Those assignments usually happen within the class
#statements you code, but they can occur anywhere you have a reference to one of the
#objects in the tree.
#Instances of the same class do not have to have the same set of attribute because instance are 
#distinct namespace!!!!!
#It's the same of global variable, in reading i go up to the three but in writing i create a new local vaiable!!!!
print('-----------------------------------------------------------------')