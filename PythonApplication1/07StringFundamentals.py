def Concatenation():
    con='a'"b"'c'
    print("'a'\"b\"'c' :" + str(con))   #Python automaticaly concatenates near string (+ is implicit)
    s='a\nb\tc\th'
    print(s)
    print("len(s): " + str(len(s)))  #7: 4 characters(a,b,c,h) + newline \n + 2 tab \t
    return;

def BlockString():          #""" .....      """
    print("BlockString: ''' dall'alba al.....        tramonto'''")
    st= """In the future 
                            there is
                                            only war"""
    u='''normale'''
    print
    print(st)
    #multiline comment
    '''
    b=a
    import sys
    print(sys.getrefcount(b))
    print(sys.getrefcount(a))
    '''
    return;

def StringForIn():
    s="Years"
    print(s)
    for x in s:
        print(x, end=' ')   #in this wai the terminator of print it's not \n but ' '
    print()
    print("'k' in s : " +str('k' in s)) #is expression is a search
    print("'e' in s : " +str('e' in s))
    return;

def IndexingAndSlicing():
    print('String are definedas immutabe ordered collection of characters')
    S= "A beautiful string"
    print(S)
    print(S[0],S[5],S[-2])
    print(S[8:15])                      #Slice take from position 8 to 15 included left bound but not right one
    print(S[8:])
    print(S[:5])
    print('S[::3] : ' + str(S[::3]))    #third parameter is the step, it take una char and then jump next two 
    print('S[::-2] : ' + str(S[::-2]))
    return;


Concatenation()
print('------------------------------------------------------------')
s= r'c:\new\file.txt'       #raw string
s1= 'c:\new\file.txt'
print(r"r'c:\new\file.txt : '" +s)
print(r'c:\new\file.txt : ' +s1)
print('------------------------------------------------------------')
BlockString()
print('------------------------------------------------------------')
StringForIn()
print('------------------------------------------------------------')
IndexingAndSlicing()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

