def VariableSwitch(a,b):       #swithc 2 variable without using a temporary variable
    a,b=b,a
    return a,b;

def UnpackingAssignment():
    a,b=10,5                    #Sequence Assignment
    print(a,b)
    a,b=VariableSwitch(a,b)
    print(a,b)
    return;

def PythonEnumerator():
    a,b,c=range(3)          #equivalent to enumerator
    print(a,b,c)
    return;

def SequenceAssignment():
    seq=[1,2,3,4,5]
    a,b,c,d,e=seq           #Sequence Assignment
    print(a,b,c,d,e)
    a,*b,c=seq                #a match the first name in the sequence, but b match everithing after that
    print("a,*b,c=seq : " + str(a)+','+str(b)+','+str(c)) #With * items number on the left and on the laft do not have tomatch 
    while seq:
        print(seq)
        left,*seq=seq
    return;

UnpackingAssignment()
print('------------------------------------------------------------')
PythonEnumerator()
print('------------------------------------------------------------')
SequenceAssignment()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')