class PersonRecord:
    def __init__(self, name, age, pay, job):
        self.name = name    
        self.age = age
        self.pay = pay
        self.job = job

    def LastName(self):
        return self.name.split()[-1]

    def GiveRaise(self, percent):
        self.pay *= (1+percent)

    def __str__(self, **kwargs):
        return "Person %s is %s years old and gain %s money" % (self.name, self.age, self.pay)



if __name__ =='__main__':
    bob = PersonRecord("Bob jr.", 23, 23000, "Doc");
    print(bob)
    bob.GiveRaise(0.3)
    print(bob)
    print(bob.LastName())



