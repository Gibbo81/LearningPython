def VariableSwitch(a,b):       #swithc 2 variable without using a temporary variable
    a,b=b,a
    return a,b;

def UnpackingAssignment():
    a,b=10,5                    #Sequence Assignment
    print(a,b)
    a,b=VariableSwitch(a,b)
    print(a,b)
    return

def PythonEnumerator():
    a,b,c=range(3)          #equivalent to enumerator
    print(a,b,c)
    return

def SequenceAssignment():
    seq=[1,2,3,4,5]
    a,b,c,d,e=seq           #Sequence Assignment
    print(a,b,c,d,e)
    a,*b,c=seq                #a match the first name in the sequence, but b match everithing after that
    print("a,*b,c=seq : " + str(a)+','+str(b)+','+str(c)) #With * items number on the left and on the laft do not have tomatch 
    while seq:
        print(seq)
        left,*seq=seq
    return

def PrintParameter(separator,eof):
    a,b,*c,d=range(10)
    print(a,b,c,d,sep=separator,end=eof)    #sep,end,fileflush must be passed as keyword argument end=...
    filew = open('.\\11files\\writestring.txt',"w") 
    print(a,b,c,d,sep=separator,end=eof,file=filew) #change output stream 
    filew.close()
    print(c,sep=separator,file=open('.\\11files\\writestringtwo.txt',"w")) 
    return

def sys_stdout():
    import sys
    sys.stdout.write('hello world2 \n')     #print() is only a simple interace to sys.stdout
    sys.stderr.write('bad '*8+"\n")     #to print error message to the standard error stream
    return

UnpackingAssignment()
print('------------------------------------------------------------')
PythonEnumerator()
print('------------------------------------------------------------')
SequenceAssignment()
print('------------------------------------------------------------')
PrintParameter(" -_- ",' FINE RIGA \n')
print('------------------------------------------------------------')
sys_stdout()
print('------------------------------------------------------------')

print('------------------------------------------------------------')