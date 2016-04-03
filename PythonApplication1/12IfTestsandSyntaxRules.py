def TestingIfSequence(value):
    if value<10:            #if,elif and else must line up vertically with the same indentation
        print(str(value) + " its' less than 10")
    elif value<20:
        print(str(value) + " its' less than 20")
    elif value<30:
        print(str(value) + " its' less than 30")
    elif value<40:
        print(str(value) + " its' less than 40")
    elif value<50:
        print(str(value) + " its' less than 50")
    elif value<60:
        print(str(value) + " its' less than 60")
    else:
        print(str(value) + " its' >= 60")
    return

def SpemmingMultipleLinee():
    a=15        #you can continue typing a statment on the next line 
    x= (a+      #if you are coding something enclosed in (), [] or {}
        6+
        7+8
        +a)
    print(x)
    if (a==15 and
        x==51 and
        x):
        print(True)        
    return

def PythonStrangeAnd_Or_pattern():
    print('Boolean expression {and, or, !} always return the left or the right object')
    print("not a simple True\False flag!!!!!")
    y=({} or 3)         #Y=3 because {} is false so the or expression return the object on yhe left size of the operation
    z=('aaa' or 15)     #z='aaa' because or does not need to evaluete 15
    z2=('aaa' and 15)   #z2 instead is 15 becaouse and need also the second condition to be evalueted
    return

def TernaryExpression(Y,Z):
    print("Also in python it's present a ternary expression (similar to c# conditional expression)")
    print(Y,Z)
    X=Y if Y>Z else Z
    print("The major number is : " + str(X))
    return

print('------------------------------------------------------------')
TestingIfSequence(0)
TestingIfSequence(25)
TestingIfSequence(50)
TestingIfSequence(159)
print('------------------------------------------------------------')
SpemmingMultipleLinee()
print('------------------------------------------------------------')
PythonStrangeAnd_Or_pattern()
print('------------------------------------------------------------')
TernaryExpression(10,6564.8)
print('------------------------------------------------------------')