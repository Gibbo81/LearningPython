def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

def ChainedCoparison():
    print('ChainedCoparison')
    a=1
    b=3
    c=5.8
    bol= a<b<c
    print('a<b<c :' + str(bol))
    bol= a<b>c
    print('a<b>c :' + str(bol))
    print('attention to floating number')
    sum=1.1+2.2
    bol= sum==3.3
    print('1.1+2.2 == 3.3 :' + str(bol))
    return

def DivisionType():
    print('True division / return always a float number')
    print('25/3 :' + str(25/3))
    print('floor division // make the truncate and ignore the remainder and return the same type of the operator')
    print('25//3 :' + str(25//3))
    print('25.2//3 :' + str(25.2//3))
    print('attention to // with negative value')
    print('it will go to the closest number below the true result')
    print('-25//3 :' + str(-25//3) + '||   -8.3333 ==> -9')   
    return

def ConversionInteger():
    print('Different base for number 64')
    print('oct(64) - hex(64) - bin(64) : ' + oct(64) + ' '+ hex(64) + ' '+ bin(64) + ' ')
    c=64
    d=oct(64)   #d is a STRING type!!!!!!!!!
    print(d)    
    i = int(d, base=8)  #back to int rom te string
    print(i)
    return

def BitwiseOperation():
    x=1
    print('x=1 :' + str(x))
    print('x<<3 :' + str(x<<3))
    print('bin(x<<3) :' + str(bin(x<<3)))
    print('x|2 :' + str(x|2))
    print('bin((x|2)) :' + str(bin((x|2))))
    print('x&1 :' + str(x&1))
    len=(x<<3).bit_length()
    print(len)
    return

def MathLibrary():
    import math         #this import work only inside the scope of this function. Outside i canno't use math.pi
    print(math.pi)
    import random
    print('random.random() :' + str(random.random()))
    print('random.randint(1,100) :' + str(random.randint(1,100)))
    print('random.choice([\'abc\',\'def\',\'hul\',\'oer\']) :' + str(random.choice(['abc','def','hul','oer'])))
    return

def Decimal():      #floating point math is less than exact
    from decimal import Decimal
    print('floating point math is less than exact')
    res = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30')
    print(res) 
    float1=12.5     # to convert from float to decimal we must first go to string
    float2=15.55
    res = Decimal(str(float1)) + Decimal(str(float2))
    print('Decimal(str(float1)) + Decimal(str(float2)) :' + str(res))
    return

def WorkingWithSet():
    print('working with set')
    s= set('abcdef')            #old 2.6 and earlier in reality it's converting from the iterable string 'spam' so 's'+'p'+'a'+'m'
    print('s = set(\'abcdef\') : '+ str(s))
    s2= set('efghil') 
    print(s.intersection(s2))
    print(s.union(s2))
    print(s.difference(s2))
    print(s.union([1,3,4,9,0])) #this commands work also with other kind of iterator
    print('\'a\' in s : ' + str('a' in s))
    #print(s+s2)  The + operator is not suppored
    s.update(s2)    #si usa al suo posto s.update()
    print(s)
    s.add('z')
    for item in s:
        print(item*5)
    s2={1,2,3,4,5}              #new 2.7 and 3X version equivalente di set(1,2,3,4,5) 
    empty=set()                 # old is used to create empty set or to convert iteable item (list....)
    fromEterabloitems=set([7,87,5,2,345,6]) #{} is still an empty dictionary
    print('set([7,87,5,2,345,6]) : ' + str(fromEterabloitems))
    return

def SetComprehensionExpression():
    from decimal import Decimal
    print('Similar to List Comprehension Expression but create a list')
    l= {x*x for x in [1,2,5,Decimal(str(8.8)),8.8,9,8] }
    print('{x*x for x in [1,2,5,Decimal(str(8.8)),8.8,9,8]} : ' +str(l))
    return

def Boolean():
    print('Boolean are a subclass of integer')
    print('True = 1  and  False=0 ')
    print('True + 10 : ' + str(True+10))
    print('True - 10 : ' + str(True-10))
    print('false + 10 : ' + str(False+10))
    print('isinstance(True,int) : ' + str(isinstance(True,int)))  #true is realy a int
    print('type(True) : ' + str(type(True)))
    return

printme("WAR")
print('Hello World')
a=2
b=4/a+3     #true division python 3.X always retains fraction reminders so the result is 5.0
print(b)
b=4/(1.0+a)
print(b)
print('------------------------------------------------------------')
ChainedCoparison()
print('------------------------------------------------------------')
DivisionType()
print('------------------------------------------------------------')
ConversionInteger()
print('------------------------------------------------------------')
BitwiseOperation()
print('------------------------------------------------------------')
MathLibrary()
print('------------------------------------------------------------')
Decimal()
print('------------------------------------------------------------')
WorkingWithSet()
print('------------------------------------------------------------')
SetComprehensionExpression()
print('------------------------------------------------------------')
Boolean()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')