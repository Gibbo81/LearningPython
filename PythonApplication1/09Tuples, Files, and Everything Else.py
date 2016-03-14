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

def UsingFiles():
    # 'r' imput, 'w' create and open, 'a' append
    #Data read from a file always come back as a string
    #similar when you write you need to pass an already formatted string
    CreateAFile()
    print('*****') 
    ReadAFile()



    return;

def CreateAFile():
    print('scrivo il file: myfile.txt') 
    writefile=open('.\\09files\\myfile.txt',"w")          # "r" imput, "w" create and open, "a" append
    writefile.write("hello text file\n")
    writefile.write("goodbye text file\n")
    writefile.close()
    return;

def ReadAFile():
    print('leggo il file: myfile.txt') 
    for line in open(r".\09files\myfile.txt"):     #r is the default
        print(line,end='')

    print('Read again with different command') 
    readfile2=open(r".\09files\myfile.txt") 
    print(readfile2.readline(),end='')
    print(readfile2.readline(),end='')
    print(readfile2.readline(),end='')
    readfile2.close()
    return;

print((40))
x=(40,)             #tu have a list of one element(useless)
print(x)
print('------------------------------------------------------------')
TupleAreImmutable()
print('------------------------------------------------------------')
TupleMethod()
print('------------------------------------------------------------')
UsingFiles()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')