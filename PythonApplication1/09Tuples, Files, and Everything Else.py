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

def BinaryFiles():
    print('leggo il file come binario') 
    data = open(r".\09files\02-Audio20CD1.ico", 'rb').read()     #rb is read binary
    print(data)
    open(r".\09files\copy02.cop", 'wb').write(data)   
    return;

def SaveObjectonFile():
    x,y=33,88.45
    s='pippo'
    dic={'a':"pluto",'b':4}
    li=[1,3,8,90,"rty"]
    file = open('.\\09files\\insertobjects.txt',"w")  
    file.write(s + '\n')
    file.write('%s,%s \n' % (x,y))              #two diferent ways to have a conversion between files
    file.write(str(dic) + ' | ' + str(li)+ "\n")
    file.close()

    filer=open('.\\09files\\insertobjects.txt')
    string=filer.readline()
    string=string.rstrip()
    print(string)
    number=filer.readline()
    splitted=number.split(',')
    print(int(splitted[0]))
    print(float(splitted[1]))
    splitted = filer.readline().rstrip().split('|')
    dictionary = eval(splitted[0])      #EVAL a build-in function that treat a string as a python expression
    list = eval(splitted[1])            #it's the same of writing  list= [...]  con l'assegnamento che è fatto dal contenuto della stringa
    print (str(list) + ' ' + str(dictionary))
    filer.close()
    return;

def UsingPickleToStoreObjectsInFile():
    print("Save a binary rappresentation of a generic object using pickle library")
    import pickle
    dic={'a':"pluto",'b':4}
    list=[1,2,3,8,9,10,"0000000000"]
    file= open('.\\09files\\pikefile.pkl',"wb")
    pickle.dump(dic,file)
    pickle.dump(list,file)
    file.close()
    
    file= open('.\\09files\\pikefile.pkl',"rb")
    dicread=pickle.load(file)
    listread=pickle.load(file)
    file.close()
    print(dicread)
    print(listread)
    return;

def UsingJsonToStoreObjectsInFile():
    print("Save a binary rappresentation of a generic object using Json library")
    import json
    dic={'a':"pluto",'b':4, 'c':45, 'aa':4353}
    file=open('.\\09files\\Jsonfile.jas',"w")
    json.dump(dic,file)
    file.close()

    file=open('.\\09files\\Jsonfile.jas')
    dicr= json.load(file)
    file.close()
    print(dicr)
    return;

def UsingStructToSaveBinaryDataOnFile():
    print("Save a binary rappresentation of a generic object using struct library")
    import struct
    int=6781223
    file=open('.\\09files\\Jsonfile.jas',"wb")
    file.write(struct.pack('@ih',4585, 17))        #@: native order, size & alignment (default) The remaining chars indicate types of args and must match exactly
    file.close()

    file=open('.\\09files\\Jsonfile.jas',"rb")
    read=file.read()
    result=struct.unpack('@ih', read)
    print(result)
    file.close()
    return;

def FileContextManager():
    print("Using with instead of close()")
    with open('.\\09files\\insertobjects.txt') as myfile:   #it's the equivalent of c# using
            for line in myfile:                             #when we exit from with il close it's automatically called
                print(line,end='')
    return;

def IsAndEqualEqual():
    x=[1,2,3,4,(9,8,7)]
    y=[1,2,3,4,(9,8,7)]
    print("x is y :" + str(x is y))  #check for object identity (reference the same object?)
    print("x == y :" + str(x == y))  #check for object equivalence 
    return;

def NoneSpecialType(): 
    lis=[None]*100  #none can be used as place older but it's also the dafault return value of a functon
    print(lis)      #that does not have a return value as this one
    lis[99]="fine"
    lis[0]='inizio'
    print(lis)
    return;

print((40))
x=(40,)             #to have a list of one element(useless)
print(x)
print('------------------------------------------------------------')
TupleAreImmutable()
print('------------------------------------------------------------')
TupleMethod()
print('------------------------------------------------------------')
UsingFiles()
print('------------------------------------------------------------')
BinaryFiles()
print('------------------------------------------------------------')
SaveObjectonFile()
print('------------------------------------------------------------')
UsingPickleToStoreObjectsInFile()
print('------------------------------------------------------------')
UsingJsonToStoreObjectsInFile()
print('------------------------------------------------------------')
UsingStructToSaveBinaryDataOnFile()
print('------------------------------------------------------------')
FileContextManager()
print('------------------------------------------------------------')
IsAndEqualEqual()
print('------------------------------------------------------------')
print(NoneSpecialType())    #the function NoneSpecialType() use return; so its default value is null
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')