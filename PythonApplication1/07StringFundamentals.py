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






Concatenation()
print('------------------------------------------------------------')
s= r'c:\new\file.txt'       #raw string
s1= 'c:\new\file.txt'
print(r"r'c:\new\file.txt : '" +s)
print(r'c:\new\file.txt : ' +s1)
print('------------------------------------------------------------')
BlockString()
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

