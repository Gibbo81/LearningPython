class FirstClass:
    MutableField=[1,2,3]                #this is an attribute present in all the istance
    #all the istance will point to the same istance, but the pointer are distinct, so change in place will
    #affect all the istance but immutable change or new assignment will affect only that singlestance
    def SetData(self, value):
        self.Data=value         #this is an attribute is created only in the current running istance
    def PrintData(self):
        print(self.Data)

class SecondClass(FirstClass):          #inheritance
    def PrintData(self):
        print("------OVERLOAD------")
        print('Overloaded method %s :-) :-)' % self.Data)





print(FirstClass.__dict__)
print('-----------------------------------------------------------------')
istance = FirstClass()
print('Class start out as an emty namespace istance.__dict__: ',istance.__dict__)   #this give out only the attribute of this istance
istance.SetData("testing")
print('But we can create new attribute in the istance ',istance.__dict__)
istance.PrintData()

print('-----------------------------------------------------------------')
istance2 = FirstClass()
istance.MutableField[1]="TTTT"  #In place change will affect all the different istance
print(istance.MutableField)
print(istance2.MutableField)
istance.MutableField=34         #not in place will affect only the current istance
print(istance.MutableField)
print(istance2.MutableField)
print('-----------------------------------------------------------------')
print('Working with inerithance')
istance3 = SecondClass()
istance3.SetData("Second is better")
istance.PrintData()
istance3.PrintData()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')