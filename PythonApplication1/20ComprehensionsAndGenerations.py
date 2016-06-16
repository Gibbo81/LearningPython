import random

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
    result=[x**2 for x in range(10) if x%2==0]   #list comprehension ara sintattically more simple
    print(result)
    print('With map and filter: list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))')
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

def GeneratorFunction(k):   #Returns an iteretor non all the set of result
    for x in range(k):      #when yield is hit it return a single result and then stop the funtion
        yield x             #it will start again when asked for a new result

def YieldFrom(k):
    yield from range(k)     #-->for i in range(k): yield i      it's the same

def GeneratorFunctionWithReturn():
    while True:
        k=random.randint(1,100)
        if k%5==0:
            yield k
            return     #return stopped the generation of new value and exit definitively from the function
        yield k

def YieldSend():
    for i in range(10): #f.send(35)
        x= yield(1)     #using the send command it's possible to send back some values to the
        print(x)        #generator function

def GeneratorExpression(n):
    ge= (x**n for x in range(10))   #similar to list comprehension but jit calculation
    print(ge)
    for i in ge:                    #the difference are () instead of []
        print(i)                    #return an iterator instead of a list of result

def permute1(seq):
	if not seq: 
		return [seq] 
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:] #removed current node and then recursive call
			for x in permute1(rest): 
			    res.append(seq[i:i+1] + x) 
		return res

def permute2(seq):  #using generator function we do not have to wait for all the data to 
	if not seq:     #be calculated. We give back the result while we get it
		yield [seq] 
	else:
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:] 
			for x in permute1(rest): 
			    yield seq[i:i+1] + x 

def SetAndDictionaryComprehension(n):
    set={x*x for x in range(n)}
    dictionary={x : x*x for x in range(n)}
    return set,dictionary

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
print('Generator function: return an iterator instead of a set of result')
result=GeneratorFunction(10)
print(next(result))       #the function return a generator object
print(result.send)
for rs in result:   #if we use them they are genereted only when needed(just in time)
    print(rs)
print('print number untill a multiple of 5 show up')
for rs in GeneratorFunctionWithReturn():
    print(rs)
print('-----------------------------------------------------------------')
print('Generator function: using send')
f=YieldSend()
next(f) #start generator necessry before the use of send(x)
print('f.send(88) : ',f.send(88))
print("f.send(35) :",f.send(35))
next(f) #this will print none because 
print('-----------------------------------------------------------------')
print("Generator Expression")
GeneratorExpression(3)
print('-----------------------------------------------------------------')
print("Generator expression and generator function are single iteration object")    #single iteration object
print('They are their own iterator so a call at iter(...) is useless')
res=GeneratorFunction(9)
print("iter(res) is res :",iter(res) is res)
seconditerator=iter(res)
print(next(res))
print(next(seconditerator)) #this one start from where the first left
print(next(res))
print('-----------------------------------------------------------------')
print(permute1([0,1,2,3,4,5]))
for x in permute2([11,22,33,44,55,77]):
    print(x, end=' *** ')
print('-----------------------------------------------------------------')
print('We can also use dictionary and set comprehension')
r1,r2=SetAndDictionaryComprehension(5)
print(r1)
print(r2)
print('-----------------------------------------------------------------')

