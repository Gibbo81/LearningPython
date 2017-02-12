def WhileLoop(word,start,stop):
    print('Printing the word little by litlle')
    while word:
        print(word,end=" ")
        word=word[1:]
    else: print("")             # this else statment run ony if the loop is exit noraly, without hitting a break block
    print('Counting from '+ str(start) + " to " +str(stop))
    while start<=stop:
        print(start,end=" ")
        start+=1
    else:
        print("")
    return

def SearchListWithElseloop(list,value):     #it would be better to use a for, but it's nly for test
    result="found"
    while list:
        if list[0]==value:
            break
        list=list[1:]
    else:
        result="not found"
    return result;

#for works on a iterator (foreach), if we want to use a more c style for we can write: 
#'for x in range(10)' --> x from 0 to 9
def ForUsing(sequence):
    print("Printing sequence ",sequence)
    for x in sequence:
        print(x,end=' ')
    else:
        print("")
    return

def IteretingOverDictionary():
    dict={'a':1,'but':"ere", 4:"eeee"}
    print('printing keys')
    for x in dict:          #it's the same of 'in dict.keys()'
        print(x)
    print('printing values')
    for x in dict.values():
        print(x)
    print('printing Items')
    for (x,y) in dict.items():      #we are using the tuple assignment that works also outside of for loop
        print(x,' -> ',y)
    return

def ExtendedSequenceAssignment(): #in practice it makes two iteration in sequence in the forassignment
    seq=[(1,2,3,4),(5,6,7,8),(9,12,14,13,16,78,4443,'1a2')]
    for (a,*b,c) in seq: #it's more eror prone, if we add another item ...,'1a2'),1] we obtein the error :1 is not iterable
        print(a,b,c)
    return

def UsingRange(start,stop, step):
    print("using range with",start,stop, step, " : ",end=" ")
    for x in range(start,stop,step):    #to make a loop thatr executs a fixed numerf times
        print(x,end=" ")
    else:
        print("")
    return

def AddOnetoEachListElement(list):  #range/len combination is usefull when we wont t change a list in place
    for x in range(len(list)):
        list[x]+=1
    return

def UsingZipLoop(listA,listB):
    dict={}
    for (x,y) in zip(listA,listB):
        print(x,y,'--',x+y)
        dict[x]=y       #it can also be used to opulate dictinaries
    return dict;

print("for works on a iterator, if we want to use a more c style for we can write: 'for x in range(10)' x from 0 to 9")
print('------------------------------------------------------------')
WhileLoop("pipperi",7,13)
print('------------------------------------------------------------')
print(SearchListWithElseloop("abcdefg",'e'))
print(SearchListWithElseloop([1,2,3,4,5,6,7,8],10))
print(SearchListWithElseloop([1,2,3,4,5,6,7,8],5))
print('------------------------------------------------------------')
ForUsing('mouse')
ForUsing((1,2,3,55,7,4,3424,453))
ForUsing([1,2,3,4,5,{'a':1,'but':"ere"},6,'ffadf',434])
print('------------------------------------------------------------')
IteretingOverDictionary()
print('------------------------------------------------------------')
ExtendedSequenceAssignment()
print('------------------------------------------------------------')
UsingRange(0,12,2)
UsingRange(7,-9,-3)
print('------------------------------------------------------------')
list=[1,2,3,9,10,-1,-3]
print("before: ",list)
AddOnetoEachListElement(list)
print("after : ",list)
print('------------------------------------------------------------')
print(UsingZipLoop([1,2,3,4,5,6],[8,7,6,-2,-3,-8]))
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')