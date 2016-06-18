class Number:
    def __init__(self, start):
        self.value = start

    def __sub__(self, other):
        return Number(self.value - other)

    def __repr__(self):
        return "The value of this number is %s" % (self.value)

    __str__=__repr__    #alias, cut out themiddleman
    #def __str__(self):
    #    return self.__repr__()

class Ind:
    l=[1,2,3,4,5]
    def __getitem__(self, index):
        return self.l[index]
    def __setitem__(self, index, value):
        self.l[3]=value

class SqaresSingleIterator:             #here we can iterate only one time
    def __init__(self, start, stop):
        self.value=start
        self.stop=stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.value>self.stop:
            raise StopIteration
        result= self.value**2
        self.value+=1
        return result

class SqaresMultiIterator:              #here we can iterate any nuber of times
    def __init__(self, start, stop):
        self.list = []
        for x in range(start,stop+1):
            self.list.append(x)

    def __iter__(self):                         #this is a ssmple scenario, in a more complex case
        return iter([x**2 for x in self.list])  #may be necessary to create an apposite class to 
    #act as my iterator: return SqareIterator(...); this class will implement __next__() method                

class SqaresMultiIteratorWithClass:              
    def __init__(self, start, stop):
        self.list = []
        for x in range(start,stop+1):
            self.list.append(x)

    def __iter__(self):                         
        return SquareIterator(self.list)        #external class as iterator

class SquareIterator:
    def __init__(self, list):
        self.list=list
        self.offset=0

    def __next__(self):
        if self.offset> len(self.list):
            raise StopIteration
        result = self.list[self.offset]**2
        offset = self.offset
        self.offset += 3    ##to change a little :-)
        return result, offset

class Contains:
    def __init__(self,list):
        self.list = list
    def __contains__(self,x):       #to enable in command
        return x in self.list
    def __repr__(self):
        return str(self.list)

class GenericAttr:
    def __init__(self):
        self.x = 39
    def __getattr__(self, attrname):
        if attrname == 'value':
            self.x+=1
            return self.x
        raise AttributeError('The attribute %s not allowed' % attrname)

class Wallet():
    def __init__(self, money):
        self.money=money
    def __str__(self):  #is tried first for the print operation and the str built-in function  It generally should return a user-friendly display
        return 'This Wallet contain %s dollar' % self.money
    def __repr__(self): #It should generally return an as-code string that could be used to re-create the object
        return "{money : %s}" % self.money

class Adder():
    def __init__(self, value):
        self.value=value
    def __add__(self, value):
        if isinstance(value,Adder):     #to check the correct use of this + implementation
            return Adder(self.value + value.value)
        raise AttributeError
    __radd__ = __add__       #cut out the middleman. __radd__ --> x+Adder(10)
    def __repr__(self): 
        return "{Value : %s}" % self.value

print('**************************************************************')
x=Number(5)
y=x-10
print(y)    
print('--------------------------------------------------------------')
print("__getitem__ method is called automatically for instance-indexing operations READING")
x=Ind()
print(x[3])
print("__setitem__ method is called automatically for instance-indexing operations SETTING")
x[3]='989'
print(x[3])
count = 0
print("__getitem__ is also used for supporting any iteration context as the for loop")
for val in x:
    print('Valore numero ', count, ' vale: ',val)  
print('**************************************************************')
print("__iter__ and __next__ are the primary way to use for cicling")
print('If they are not present python call __getitem__ as a second class solution')
s = SqaresSingleIterator(1,10)
for x in s:
    print(x)  
for x in s:     #this only workone time than it's not repitable
    print(x)         
print('--------------------------------------------------------------')
print('If you wish you can made it work anby number of time!!!')
multi = SqaresMultiIterator(1,10)
for x in multi:
    print(x)    
print("This can be used any number of time!!!!!!") 
for x in multi:
    print(x)   
print('Again and again')  
for x in multi:             #are totally indipendent
    for h in multi:
        print(x, " + ", h)     
print('**************************************************************')
print('Same as before but using an external classes as iterator')
h=SqaresMultiIteratorWithClass(1,10)
for x,y in h:
    print('Square of offset %s has value %s' % (y,x))
print('--------------------------------------------------------------')
u=Contains([1,2,3,4,56,7,8,9])
print('u:',u) 
print("4  in u: ",4  in u)
print('99 in u: ',99 in u)
print('**************************************************************')
ga = GenericAttr()
print(ga.value)
print(ga.value)
try:        
    print(ga.valuenotpresent)
except Exception as e:
    print(e)
    print("Error valuenotpresent is not a recognized field")         
print('--------------------------------------------------------------')
y=Wallet(798)
print(y)
print(y.__repr__())
print('**************************************************************')
a= Adder(15)
b= Adder(86)
print (a+b)
print('--------------------------------------------------------------')

print('**************************************************************')

print('--------------------------------------------------------------')