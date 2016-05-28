from decimal import Decimal

class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay= Decimal(str(pay))

    def PayRaise(self,x):
        self.pay*=Decimal(str(x))

    def GetLastName(self):
        return self.name.split()[1]

    def __repr__(self):
        return "My name is %s and I work as %s" % (self.name, self.job)

    def __str__(self):
        return self.__repr__()

class Manager(Person):
    def PayRaise(self,x,ManagerBonus=1.1):      #we can call the implemantation of the base class. 
        Person.PayRaise(self,x*ManagerBonus)    #A class’s method can always be called either through
                                                #an instance or through the class (where you must pass 
                                                #theinstance manually).




if __name__=='__main__':
    bob = Person('Bob Dil')
    susan= Person("Susan Patrick","robber",841)
    print(bob.name,bob.pay)
    print(susan.name,susan.pay)
    print("bob.GetLastName(): ",bob.GetLastName())
    susan.PayRaise(1.12)
    print("Susan pay rise!")
    print(susan.name,susan.pay) 
    print(susan)
    print('********************************************')
    boss= Manager("theone",'boss',100)
    boss.PayRaise(2)
    print(boss.pay)
    print('********************************************')

    print('********************************************')

    print('********************************************')

    print('********************************************')

