def printing(a,b,c): print(a,b,c)

def DefaultPrinting(a,b='second default',c="third default"): print(a,b,c)

def MutableDefault(a,b=[]): #ATTENTION!!!!!!! b reuse always the same istance of default []
    b.append(a)             #b IS NOT RESET on successive call
    print(b)                #do not use mutable default variable!!!!!!!!!
    #ci sta se uno pensa al def come ad un'assegnamento che quando viene eseguito salva anche i parametri di default


print("Parameter can be match by keyword and not only by position")
printing(b="secondo",c=' finale',a='primo')
printing("primo",c=' finale',b="secondo")
print('-----------------------------------------------------------------')
print('Using default parameter')
DefaultPrinting('_questo lo passo io_')   #using default + keyword parameters we can assign data to the function in more or less any way we like
DefaultPrinting('_questo lo passo io_',c="Anche l'ultimo lo passo io")  
print('-----------------------------------------------------------------')
MutableDefault(1)
MutableDefault('Manual b assigned',['explicit'])    #an explicit assignment do not change the use of default mutable parameter
MutableDefault('donaldduck')
MutableDefault([76,78,77,234])
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')