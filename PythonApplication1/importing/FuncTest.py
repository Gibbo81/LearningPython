def PrintValue(value):
    print(value)
    return

def Intersect(a,b):
    result={x for x in a if x in b}  #set to avoid duplication
    '''
    result=[]
    for x in a:
        if x in b:
            result.append(x)
    '''
    return result

def NoneReturning():
    print("this functon does nothing and return default")
    return






