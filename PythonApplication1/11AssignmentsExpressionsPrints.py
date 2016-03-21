def VariableSwitch(a,b):       #swithc 2 variable without using a temporary variable
    a,b=b,a
    return a,b;

def UnpackingAssignment():
    a,b=10,5
    print(a,b)
    a,b=VariableSwitch(a,b)
    print(a,b)
    return;

def PythonEnumerator():
    a,b,c=range(3)          #equivalent to enumerator
    print(a,b,c)
    return;


UnpackingAssignment()
print('------------------------------------------------------------')
PythonEnumerator()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')