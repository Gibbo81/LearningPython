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
        return "My name is %s and I work as %s for %s" % (self.name, self.job, self.pay)

    __str__=__repr__    #alias, cut out themiddleman
    #def __str__(self):
    #    return self.__repr__()

class Manager(Person):
    def __init__(self, name, pay = 0):
        Person.__init__(self, name, 'Boss', pay)
        #super().__init__(name, 'Boss', pay)  #It's the samre with super but we do not chose wich super class call

    def PayRaise(self,x,ManagerBonus=1.1):      #we can call the implemantation of the base class ANY BASE CLASS!!! 
        Person.PayRaise(self, x*ManagerBonus)   #A class’s method can always be called either through
                                                #an instance or through the class (where you must pass 
                                                #theinstance manually).
    def __repr__(self):
        return "**MANAGER** "+ Person.__repr__(self) 

    def __str__(self):
        return self.__repr__()

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
    boss= Manager("theone",100)
    boss.PayRaise(2)
    print(boss.pay)
    print('********************************************')
    print("We can use polimorfism without explicit seclaration")
    print('Print all')
    for obj in (bob,susan,boss):    #polymorphism is used witout nothing that explicity aggregate different class
        print(obj)                  #in c# we would need at last a common interface
    print('********************************************')