def Concatenation():
    con='a'"b"'c'
    print("'a'\"b\"'c' :" + str(con))   #Python automaticaly concatenates near string (+ is implicit)
    s='a\nb\tc\th'
    print(s)
    print("len(s): " + str(len(s)))  #7: 4 characters(a,b,c,h) + newline \n + 2 tab \t
    return

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
    return

def StringForIn():
    s="Years"
    print(s)
    for x in s:
        print(x, end=' ')   #in this wai the terminator of print it's not \n but ' '
    print()
    print("'k' in s : " +str('k' in s)) #is expression is a search
    print("'e' in s : " +str('e' in s))
    return

def IndexingAndSlicing():
    print('String are definedas immutabe ordered collection of characters')
    S= "A beautiful string"
    print(S)
    print(S[0],S[5],S[-2])
    print(S[8:15])                      #Slice take from position 8 to 15 included left bound but not right one
    print(S[8:])
    print(S[:5])
    print(S[:0])
    print('S[::3] : ' + str(S[::3]))    #third parameter is the step, it take una char and then jump next two 
    print('S[::-2] : ' + str(S[::-2]))
    return

def CommonUsedMethod():
    y='spammy'
    print(y.replace('am',"omo"))
    print(y.find('my'))
    print(y.find('mym'))        #-1 if it doesn't found nothing

    lis=list(y)
    print(lis)
    back='-'.join(lis)      #- is put between each element it will concatenate
    print(back)

    y=" bob*$john*$arthur*$li nd "
    print(y.split('*$'))
    print(y.strip())
    return

def FormattingExpression():
    print("Formatting expression")
    print('That is {0} {1} bird!'.format(1,"dead"))     #new way sobstitution
    print('%d %s %g you' % (1, 'spam', 4.0))            #old way sobstitution
    print(r"%d: integer -- %g: float -- %s Convert to string (more or less everithing")
    print('All whith \%: ' +  '%s %s %s you' % (1, 'spam', 4.0))  
    return

def DictinaryBaseFormattingExpression():
    dict={"qty":1, "b":2,"c":3,"d":4}   
    str="prova %(qty)d inserisce - %(d)s"   
    print(str % dict )          # inserisci il valore del dizionario che ha come chiave d trattandolo con il passaggio %s (conversione a stringa)
    return

def StringFormattingMethod():
    template = 'Inseriamone tre: {0}, {1}, {2}'     #by position
    template2 = 'Inseriamone tre: {}, {}, {}'       #by relative position
    print(template.format('un',"dos",'tres'))
    print(template2.format('un',"dos",'tres'))
    return


Concatenation()
print('------------------------------------------------------------')
print('raw string')
s= r'c:\new\file.txt'                                       #raw string
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
FormattingExpression()             #format method
print('------------------------------------------------------------')
CommonUsedMethod()
print('------------------------------------------------------------')
print('------------------------------------------------------------')
DictinaryBaseFormattingExpression()
print('------------------------------------------------------------')
StringFormattingMethod()
