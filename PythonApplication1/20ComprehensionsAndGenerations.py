def ThreeWays():
    string='spam'
    res=[]
    for x in string:
        res.append(ord(x))
    print(res)
    res = list(map(ord,string))
    print(res)
    res=[ord(x) for x in string]
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

print('-----------------------------------------------------------------')
print("Now we have 3 ways to apply an expression to all items inside an iterable")
print('for cicle, map function and list Comprehension')
ThreeWays()
print('-----------------------------------------------------------------')
FilterAndExpression()
print('-----------------------------------------------------------------')
MultipleSorceData()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')