def BasicListOperations():
    print('BasicListOperations')
    li=["a",'b']
    li.append([1,4,8])
    print(li+['z'])                     # +
    print(li*3)                         # *
    bool='a' in li                      # in
    print(bool)
    for x in li:                        # for
        print(x, end= '  ')
    print()
    res= [x*2 for x in li]              #list comprehension
    print(res)
    '''
    mapper= map(abs,[1,2,3,4,-8,-9,-154])
    print(mapper)
    '''
    return;

def Indexing():
    print('Indexing')
    lis=[1,5,[11,44,77,[179,139]],9]
    res=lis[2:]
    print(res)
    value179 = res[0][-1][0]             #list can ontains other list sometime we need more than one index operator
    print(value179)
    matrix= [[1,2,3],                    #can spam multiple lines
             [4,5,6],
             [7,8,9]]
    return;

def ChangeAValue(list, index, value):
    list[index]=value
    return;

def InPlaceChange():
    print("InPlaceChange")
    lis=[1,2,3,4]
    ChangeAValue(lis,-1,'New value')    # Index assignment: change a single valure
    print(lis)      
    lis[1:3]=[-999,-998, -997, -996]    # Slice assignment: change a block with slice assignment--> first a deletion and then a new insertion
    print(lis)
    lis[1:2]=[]                           # this can be considered a deletion but only work on slice assignment
    lis[2]=[]                             # this only assi to position [2] a reference to an empty object   
    del lis[1]                            # questo cancella veramente la posizione [1]
    lis[1:1]=[44,45]                      # and this an insertion
    print(lis)
    
    lis.append('append a single object')    #add an object
    lis.extend(["take a list",8,4,0])       #add a list of object
    print(lis)
    lis.insert(1,'posizione uno [1]')       # add the object in the specific position
    print(lis)
    return;

def ListMethod():
    li=[1,2,1,13,4,'appo']
    print(li.index(1))
    print(li.count(1))    
    return;

def BasicDictionaryOperator():
    print("start with dictionary")
    di={'a':1,"b":2,'c':3, 4:'quattro'}
    print(di)
    print("di['c'] : "+ str(di['c']))
    print("di[4] : "+ str(di[4]))
    di={'a':1,'b':2,'c':3, 'd':{"zz":12,'vv':34}}
    print(di)
    print('di["d"]["vv"] : ' + str(di["d"]["vv"]))
    print("len(di) : " + str(len(di)))
    keys=di.keys()                                  # type is dict_keys
    print(keys)
    print(list(keys))                               # if we want a list we should uselist(...) 
    print('"b" in di : ' + str("b" in di))          #check if a key with this value is present into the dictionary
    print('"y" in di : ' + str("y" in di))
    return;

BasicListOperations()
print('------------------------------------------------------------')
Indexing()
print('------------------------------------------------------------')
InPlaceChange()
print('------------------------------------------------------------')
ListMethod()
print('------------------------------------------------------------')
BasicDictionaryOperator()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')