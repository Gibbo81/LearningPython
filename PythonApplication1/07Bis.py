def DictinaryBaseFormattingExpression():
    dict={"qty":1, "b":2,"c":3,"d":4}   
    str="prova %(qty)d inserisce - %(d)s"   
    print(str % dict )          # inserisci il valore del dizionario che ha come chiave d trattandolo con il passaggio %s (conversione a stringa)
    return;

def StringFormattingMethod():
    template = 'Inseriamone tre: {0}, {1}, {2}'     #by position
    template2 = 'Inseriamone tre: {}, {}, {}'       #by relative position
    print(template.format('un',"dos",'tres'))
    print(template2.format('un',"dos",'tres'))
    return;

print('------------------------------------------------------------')
DictinaryBaseFormattingExpression()
print('------------------------------------------------------------')
StringFormattingMethod()

