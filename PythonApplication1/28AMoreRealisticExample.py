import person
import shelve

def ReadFromShelve(path):
    reader=shelve.open(path)
    print('number of records: ',len(reader))
    
    for key in reader:    #same as: for x in reader.keys():  
        print(reader[key])
    reader.close()




print('********************************************')
bob= person.Person('Bob Smith')
print("bob.__class__: ", bob.__class__)
print("bob.__class__.__name__: ", bob.__class__.__name__)
boss= person.Manager("TheOne",100)
print("boss.__class__.__bases__: ", boss.__class__.__bases__)   #all the superclass
print('--------------------------------------------')
print('Storing object in a shelve DB')
pippo= person.Person("Goofy",'Discontinuos',10)
topolino=person.Person("Mouse",'Detective',44)
basettoni=person.Manager("Seamus O'Hara",100)

dbopened=shelve.open(".\\28files\\newshelvefile")
for obj in (pippo,topolino,basettoni):
    dbopened[obj.name]=obj
    print("saved: ",obj.name)
dbopened.close()
print("Let's add more people")

top=person.Person("Test",'--')
top2=person.Person("Test2",'****',1)
dbopened=shelve.open(".\\28files\\newshelvefile")
for obj in (top,top2):
    dbopened[obj.name]=obj      #this is the write command!
    print("saved: ",obj.name)
dbopened.close()
print('********************************************')
print('Now read data from our db files')
ReadFromShelve(".\\28files\\newshelvefile")
print('--------------------------------------------')
print("Load change an object and save it back")
rw=shelve.open(".\\28files\\newshelvefile")
goofy=rw["Goofy"]
goofy.PayRaise(9)
rw["Goofy"]=goofy
rw.close()
ReadFromShelve(".\\28files\\newshelvefile")
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











