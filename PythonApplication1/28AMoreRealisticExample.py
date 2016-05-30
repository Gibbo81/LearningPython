import person



print('********************************************')
bob= person.Person('Bob Smith')
print("bob.__class__: ", bob.__class__)
print("bob.__class__.__name__: ", bob.__class__.__name__)
boss= person.Manager("TheOne",100)
print("boss.__class__.__bases__: ", boss.__class__.__bases__)   #all the superclass
print('--------------------------------------------')

print('********************************************')

print('--------------------------------------------')

print('********************************************')
    
print('--------------------------------------------')

print('********************************************')


'''
To minimize the chances of name collisions like this, Python programmers often prefix
methods not meant for external use with a single underscore: _gatherAttrs in our case.
This isn’t foolproof (what if another class defines _gatherAttrs, too?), but it’s usually
sufficient, and it’s a common Python naming convention for methods internal to a class.
A better and less commonly used solution would be to use two underscores at the front
of the method name only: __gatherAttrs for us. Python automatically expands such
names to include the enclosing class’s name, which makes them truly unique when
looked up by the inheritance search.
'''











