def TupleAreImmutable():
    t=(1,2,3,['w','e','r','t'])
    print(t)
    #t[3]=65  This is an error ==> 'tuple' object does not support item assignment
    t[3][1]=111     #but if a tuple has inside a mutable object, in this case a list it's possible to change it chenging in reality the basic tupla  
    print(t)
    return;

def TupleMethod():
    t=(1,2,3,4,5,6,2,7,8,9,2)
    print(t)
    print('t.count(2) :' + str(t.count(2)))
    print('t.index(2,2) :' + str(t.index(2,2)))

    return;




print((40))
x=(40,)             #tu have a list of one element(useless)
print(x)
print('------------------------------------------------------------')
TupleAreImmutable()
print('------------------------------------------------------------')
TupleMethod()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')