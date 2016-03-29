def ManualIteration(path, list):
    print('manual iteration: f.__next__ and next(f)')
    with open(path) as f: #a file object is its own iterator
        while True:
            try:
                print(f.__next__().rstrip())    #f.__next__() and next(f) are the same in python 3.X
            except StopIteration:
                break
        print()     
    
    iterator=iter(list)    #a list supports multiple open iterator so they are not their own iterator
    while True:            #we must obtein it before if we are working by hands
        try:
            print(next(iterator),end="  ") 
        except StopIteration:
            break
    print()
    return;




#Any object with a __next__ method to advance to a next result and which raises StopIteration at the end of 
#a series result is considered an iterator.
#all iterator tool work by calling __next__ an catching StopIteration  to determine when to exit.
print('------------------------------------------------------------')
for line in open(r".\09files\myfile.txt"):  #the file its a classic iterator
    print(line,end='')    
print('------------------------------------------------------------')
ManualIteration(r".\09files\myfile.txt",[1,2,'rty'])
print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')

print('------------------------------------------------------------')