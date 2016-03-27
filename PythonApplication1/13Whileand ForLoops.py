def WhileLoop(word,start,stop):
    print('Printing the word little by litlle')
    while word:
        print(word,end=" ")
        word=word[1:]
    else:               #run ony if the loop is exit noraly, without hitting a break block
        print("")
    print('Counting from '+ str(start) + " to " +str(stop))
    while start<=stop:
        print(start,end=" ")
        start+=1
    else:
        print("")
    return;

def SearchListWithElseloop(list,value):     #it would be better to use a for, but it's nly for test
    result="found"
    while list:
        if list[0]==value:
            break
        list=list[1:]
    else:
        result="not found"
    return result;

def ForUsing(sequence):
    print("Printing sequence ",sequence)
    for x in sequence:
        print(x,end=' ')
    else:
        print("")
    return;

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
    return;

def ExtendedSequenceAssignment(): #in practice it makes two iteration in sequence in the forassignment
    seq=[(1,2,3,4),(5,6,7,8),(9,12,14,13,16,78,4443,'1a2')]
    for (a,*b,c) in seq: #it's more eror prone, if we add another item ...,'1a2'),1] we obtein the error :1 is not iterable
        print(a,b,c)
    return;

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

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')