def RecursivSum(l):
    print(l)    #remeber an empty object is always False
    return 0 if not l else l[0]+RecursivSum(l[1:])  #conditional expression in python

def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
        else:
            tot += sumtree(x) # Recur for sublists
    return tot







print(RecursivSum([1,2,3,4,5,6,7,8,9]))
print(RecursivSum([]))
print('-----------------------------------------------------------------')
print('Using recursive to access any Arbitrary nesting structure')
L = [1, [2, [3, 4, 5 , [1 , 65, 999]], 5], 6, [7, 8]] 
print(sumtree(L)) 
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')