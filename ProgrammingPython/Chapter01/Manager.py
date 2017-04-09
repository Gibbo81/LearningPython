from Person import PersonRecord

class Manager(PersonRecord):
    role = 'Manager'
    def __init__(self, name, age, pay):
        PersonRecord.__init__(self, name, age, pay, Manager.role)
        #super().__init__(name, age, pay,"manager") 
        #It's the same effect but we do not chose which super class we are going to call

    def GiveRaise(self, percent, managerBonus=0.1):
        PersonRecord.GiveRaise(self,percent+managerBonus)

if __name__ =='__main__':
    boss= Manager("big Boss",67,50000)
    boss.GiveRaise(0.5)
    print(boss) 