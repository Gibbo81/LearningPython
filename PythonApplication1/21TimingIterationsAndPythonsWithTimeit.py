import timeit #library for time check

def TestListComprehension():
    return [x**2 for x in range(1000)]



print('-----------------------------------------------------------------')
print('try the use of timeit.repeat')
result=timeit.repeat(stmt="[x**2 for x in range(1000)]",    #repeat this function 
                     number=1000,                           #for 1000 times
                     repeat=5)                              #this check is executed five different times
count=1
for x in result:
    print("the attempt",count,"use",x,"seconds")
    count+=1
print('-----------------------------------------------------------------')
print('try the use of timeit.repeat with function call')
TestListComprehension()
count=1
result=timeit.repeat(stmt="TestListComprehension()",                        #to use a defined functione i have to import it
                     setup="from __main__ import TestListComprehension",    #in a explicit way, this i run as a setup before the test start
                     number=1000,                                           
                     repeat=5)      
                     
for x in result:
    print("the attempt",count,"use",x,"seconds")
    count+=1
print('-----------------------------------------------------------------')
print('try to call directly the function')
TestListComprehension()
count=1
result=timeit.repeat(stmt=TestListComprehension,  #or we can call directly the function
                     number=1000,                                           
                     repeat=5)      
                     
for x in result:
    print("the attempt",count,"use",x,"seconds")
    count+=1
print('-----------------------------------------------------------------')
print('try the use of timeit.timeit')
print("it is the same but it repeat the test only one time")
result=timeit.timeit(stmt=TestListComprehension,  #or we can call directly the function
                     number=1000)
print("The result of timeit.timeit is: ",result)
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')













