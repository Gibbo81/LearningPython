def printing(a,b,c): print(a,b,c)

def DefaultPrinting(a,b='second default',c="third default"): print(a,b,c)

#ATTENZIONE ATTENZIONE ATTENZIONE ATTENZIONE ATTENZIONE ATTENZIONE ATTENZIONE ATTENZIONE
def MutableDefault(a,b=[]): #ATTENTION!!!!!!! it reuses always the same istance of default []
    b.append(a)             #b IS NOT RESET on successive call
    print(b)                #do not use mutable default variable!!!!!!!!!
                            #default argument values are evalueted and saved once when a def statment is run 
                            #not each time the resultig function is called 

def CollectingArgumentTuple(first,*args): #all the arguments except the first went into the tuple
    print(args)
    return args

def CollectinArgumentDictionary(a,**dict):  #all the key parameter are groupped inside dict
    for x in dict.values():                 #of course not the parameter a=......
        print(x, end=' ')
    print()                              
    return dict

def UnpckingArgument(a,b,c,d):
    print(a,b,c,d)

def Sum(a,b,c,d):
    return a+b+c+d

def Tracer(func,*tupl,**dict):
    print('Calling ',func.__name__)
    return func(*tupl,**dict)

def KeywordOnlyArgument3(a,*b,c):    #c is a keyword only must always be pass using (...,c=...)
    print(c)  

def KeywordOnlyArgument(a,*b,c='default'):    #c is a keyword only must always be pass using (...,c=...)
    print(c)                                  #unless of course we ut a default value  

def KeywordOnlyArgument2(a,*,c='default'):  #same as before but the functio do not accept a variable-lenght argument list 
    print(c)

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
print('Any of this parameter after the first is put inside the *args')
result=CollectingArgumentTuple(9,54,"ertr",{'a':13,'tu':"err"})
seconds=CollectingArgumentTuple({'y':13,'ufew':"err"})
print('Any keyword parameter except "a" is put inside the **dict')
result=CollectinArgumentDictionary(12,t=13,y=76,h='pool')
seconds=CollectinArgumentDictionary(t=13,a=999999,y=76)
third=CollectinArgumentDictionary(a=999999)
print('-----------------------------------------------------------------')
print('We can use this method also in the caller to unpack a list fun(*list)')
list=(15,89,875,'rrr')
UnpckingArgument(*list)
#list=(15,89,875,'rrr',7777)    #this give an error. nmber of attribute must be correct
#UnpckingArgument(*list)        #it's ore or less useless why not to put a tuple as parameter?
print('-----------------------------------------------------------------')
print('We can use prameter to call function in indirect way')
print(Tracer(Sum,12,58,87,d=4))
#print(Tracer(Sum,12,58,87,b=4)) #this of course give an error because we have multiple values for parameter b
print('-----------------------------------------------------------------')
print('Using Keyword Only Argument')
KeywordOnlyArgument(1,2,3,4,5,c="print me") #if we use *b c=... must be at the end
KeywordOnlyArgument(1,2,3,4,5,7,'f')
KeywordOnlyArgument3(1,2,3,4,5,7,'f',c='pippo')
#KeywordOnlyArgument3(1,2,3,4,5,7,'f')      #this give error because c is not present
KeywordOnlyArgument2('a')
KeywordOnlyArgument2(c='prent me 2',a='ttt')
print('-----------------------------------------------------------------')