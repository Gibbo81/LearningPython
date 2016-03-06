def BasicListOperations():
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
    lis=[1,5,[11,44,77,[179,139]],9]
    res=lis[2:]
    print(res)
    value179 = res[0][-1][0]             #list can ontains other list sometime we need more than one index operator
    print(value179)
    matrix= [[1,2,3],                    #can spam multiple lines
             [4,5,6],
             [7,8,9]]

    return;






BasicListOperations()
print('------------------------------------------------------------')
Indexing()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')