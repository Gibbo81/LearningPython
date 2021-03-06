def BasicListOperations():
    print('BasicListOperations')
    li=["a",'b']
    li.append([1,4,8])
    print(li+['z'])                     # + similar to append!!!!
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
    return

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
    return

def ChangeAValue(list, index, value):
    list[index]=value
    return

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
    return

def ListMethod():
    li=[1,2,1,13,4,'appo']
    print(li.index(1))
    print(li.count(1))    
    return

def BasicDictionaryOperator():                      #key any immutable object work fine
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
    print(list(di.values()))
    print(list(di.items()))
    di2=di.copy()                                   #create a different copy, if we change di2 di remanes the same
    del di2['d']
    print(di)
    print(di2)
    return

def DictionaryChangeInPlace():
    D={'eggs':3,'spam':2,'ham':1}
    print(D)
    D['ham']=["grill","bake","fray"]
    print(D)
    del D['eggs']
    print(D)
    D["NEW ENTITY"]=12                          #if the key is not present we add a new entity
    print(D)
    return

def DictionaryExample():
    table = {'1975': 'Holy Grail', 
             '1979': 'Life of Brian',
              1983 : 'The Meaning of Life'}
    year='1979'
    print(table[year])
    for x in table:                             # same as => for x in table.keys():          
        print(str(x) + " : " + str(table[x]))    
    for key in table:                           # same as => for x in table.keys():   
        print(table[key])    
    #to use the dictionary in revers order starting from the value to obtasin the key
    print([years for (years,title) in table.items() if title=='The Meaning of Life'])
    return

def Comprehension():
    print("Comprehension for building dictionary")
    D={k:v for (k,v) in zip(['a','b',"c"],[1,2,3])}
    print(D)
    D={x:x*4 for x in [0,1,2,3,5,9,100] if x%2==0}
    print(D)
    D={x.lower():x for x in "SPAMMER"}
    print(D)
    return

def ViewObject():
    print("In 3.X we have not list for .keys() but view object")
    table = {   '1975': 'Holy Grail', 
                '1979': 'Life of Brian',
                1983 : 'The Meaning of Life'}
    print(type(table.keys()))                       #dict_keys is an iterable object not a list
    print(type(table.values()))
    print(type(table.items()))
    print("We can cast to list using list(...)")
    print(list(table.keys()))
    print(list(table.values()))
    print(list(table.items()))
    print("this view are pointer so if the base dictionary change they reflect this change!")
    items=table.values()
    table[2010]="A good year"
    for x in items:
        print(x)
    print('It\'s print the new one, but it vas created before :-)')
    return

def SortingDictionary():
    dic={'e':4,
         'a':1,
         'b':2,
         'c':3,}
    print('Dictionary order is not deterministic: ')
    print(dic)
    print('but we can use .sort(..) to sort its keys')
    keylist=list(dic.keys())
    for x in sorted(keylist,reverse=False):
        print(dic[x])
    #equivalent
    keylist.sort(reverse=True)      #use compare func if given
    for x in keylist:
        print(dic[x])
    return

def DictionaryIn():
    dic={'e':4,
         'a':1,
         'b':2,
         'c':3,}
    print(dic)
    print("'b' in dic : " + str('b' in dic))
    print("'b' in .keys() : " + str('b' in dic.keys()))  #it's the same check
    print("'5' in dic.values() : " + str('5' in dic.values()))
    return


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
DictionaryChangeInPlace()
print('------------------------------------------------------------')
DictionaryExample()
print('------------------------------------------------------------')
Comprehension()
print('------------------------------------------------------------')
ViewObject()
print('------------------------------------------------------------')
SortingDictionary()
print('------------------------------------------------------------')
DictionaryIn()
print('------------------------------------------------------------')
fieldnames = ('name', 'age', 'job', 'pay')
for [ix, label] in enumerate(('pippo',) + fieldnames):
    print( ix, ' --- ', label)
