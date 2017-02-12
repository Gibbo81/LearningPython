def ListAdd(lista):
    lista.append(3)
    return

def IntSum(intero):
    return intero+3;

def TwoEqualityCheck():
    print('two different type of comparisation')
    a=[1,2,3]
    b=a
    print(b==a)         #check if the value is the same
    print(b is a)       #check if the referred object is the same (link to the same object)
    b=[1,2,3]           #same value but different object
    print(b==a)
    print(b is a)

    b=a
    import sys
    print(sys.getrefcount(b))
    print(sys.getrefcount(a))
    return

l1=[]  #list mutable
print(l1)
ListAdd(l1)
print(l1)
ListAdd(l1)
print(l1)
l2=l1
l2[0]='55'
print(l1)
#------------------------
i=7     #number immutable {as string and tuple}
print(i)
i=IntSum(i)
print(i)
i=IntSum(i)
print(i)
print('------------------------------------------------------------')
TwoEqualityCheck()
print('------------------------------------------------------------')