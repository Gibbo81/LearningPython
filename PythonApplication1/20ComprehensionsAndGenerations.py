def ThreeWays():
    string='spam'
    res=[]
    for x in string:                #for
        res.append(ord(x))
    print(res)
    res = list(map(ord,string))     #map eduction
    print(res)
    res=[ord(x) for x in string]    #list comprehension
    print(res)

def FilterAndExpression():
    print('With list Comprehension [x**2 for x in range(10) if x%2==0]')
    result=[x**2 for x in range(10) if x%2==0]
    print(result)
    print('With ma+ and filter: list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))')
    result=list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))
    print(result)

def MultipleSorceData():    
    print('We can have more than one source inside list comprehension')
    res=[x+y for x in [0,1,2,3]         #this works as 2 nested for loops
             for y in [100,200,300]]
    print(res)

def DoublweForStatment():     #work with matrix
    matrix=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    print('Matrix: ',matrix)
    print("we will add 10 to each element")
    matrix=[[x+10 for x in row] for row in matrix]
    print('Matrix: ',matrix)
    matrix=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    print('Matrix: ',matrix)
    print("we will add 10 to each element and linearize the matrix")
    matrix=[x+10 for row in matrix for x in row]   #double for statmnet 
    print('A single list Matrix: ',matrix)




print('-----------------------------------------------------------------')
print("Now we have 3 ways to apply an expression to all items inside an iterable")
print('for cicle, map function and list Comprehension')
ThreeWays()
print('-----------------------------------------------------------------')
FilterAndExpression()
print('-----------------------------------------------------------------')
MultipleSorceData()
print('-----------------------------------------------------------------')
print(list(range(10)))
print('-----------------------------------------------------------------')
DoublweForStatment()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')