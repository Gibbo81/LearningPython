from tkinter import Button, mainloop

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

def AddAttribute():
    sumtree.count=10
    sumtree.handles="Pressing"
    print("sumtree.handles: ",sumtree.handles) 
    print("sumtree.count: ",sumtree.count) 
    print("dir(sumtree): ",dir(sumtree))    #with dir(...) we can explore detail of object

exp= lambda x=10,y=29: x+y  #lambda is always a single expression, it cann't spam on more lines
li=[lambda x: x**2,         #lambda can work here because is a statement not an expresson (return a value)
    lambda x: x**3,
    lambda x: x**4]
noargexp = lambda: print('No argument') 

print(RecursivSum([1,2,3,4,5,6,7,8,9]))
print(RecursivSum([]))
print('-----------------------------------------------------------------')
print('Using recursive to access any Arbitrary nesting structure')
L = [1, [2, [3, 4, 5 , [1 , 65, 999]], 5], 6, [7, 8]] 
print(sumtree(L)) 
print('-----------------------------------------------------------------')
print('Function attribute: it"s possible o add attribute to function')
AddAttribute()
print('-----------------------------------------------------------------')
print("Lambda function")
print("exp(3,2) :",exp(3,2))
print('exp() :',exp())
print('li[1](10) :',li[1](10))
print('-----------------------------------------------------------------')
b= Button(text='Press me', command=(lambda:print('spamming'))) #we can use lambda inside the call back (here a GUI)
b.pack()
mainloop()
print('-----------------------------------------------------------------')
print('Map')
li=[1,2,5,9,880]
li=list(map(lambda x: x+10, li))    #map calls the passing function (here a lambda) on each element of the list and return an iterable
print(li)
se1=('a','b','c')
se2=(1,2,3)
print(list(map(lambda x,y: str(x)+' '+str(y), se1, se2)))   
#if map's function take more than 1 argument we can pass 2 list of values
print('-----------------------------------------------------------------')
from functools import reduce
print('Filter and Reduce')
print(list(filter(lambda x: x>0, range(-5,5)))) #similar to map it return only the value that are valid (here >0)
print(reduce(lambda x,y: x+y, (1,2,3))) #at each step reduce passes the current result along with the next result from list
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')