import InitialData as ID
import pickle
import os
import glob
import shelve

def PersistDBOnFile(filename, object):
    with open(filename, 'wb') as dbfile:
        pickle.dump(object, dbfile)

def ReadDbFromPersistingFile(filename):
    with open(filename, 'rb') as openf:
        return pickle.load(openf)

def SaveInFolder(foldername, object):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    for key in object:
        PersistDBOnFile('recordfolder\\' + key + '.pkl', object[key])

def ReadAllPklFiles(folder): 
    for filename in glob.glob(folder + '\*.pkl'):
        c = ReadDbFromPersistingFile(filename)
        print(c)

def SaveWithShelve(filesname, object):
    with shelve.open(filesname) as db:
        for key in object:
            db[key] = object[key]


print('------------------------------------------------------------')

db = ID.GiveDb()
PersistDBOnFile('people', db)
db= None
db = ReadDbFromPersistingFile('people')
db['sue']["pay"] = db['sue']["pay"] * 1.2
db['red']["name"] = 'red Yellow'
PersistDBOnFile('people', db)
print(ReadDbFromPersistingFile('people'))

print('------------------------------------------------------------')

print("Save each record on it's own file")
folder = 'recordfolder'
SaveInFolder(folder,ID.GiveDb())

print("Read all the records")
ReadAllPklFiles('recordfolder')

print("change sue's record")
sue = ReadDbFromPersistingFile('recordfolder\sue.pkl')
sue['age']=30
PersistDBOnFile('recordfolder\sue.pkl',sue)

ReadAllPklFiles('recordfolder')
print('------------------------------------------------------------')

print("Save using shalve")
SaveWithShelve('peopleshelve', ID.GiveDb())

with shelve.open('peopleshelve') as sf:
    red = sf['red']
    red['pay']=89
    sf['red'] = red     #we always need to change the hightest level inside shelve db
    listr = [value for value in  sf.values()]
    dictr = {key:sf[key] for key in sf.keys()}
    
print('list: %s' % listr)
print('dict: %s' % dictr)
print('------------------------------------------------------------')

print('Using class to rappresent records')
from Person import PersonRecord
from Manager import Manager

p1 = PersonRecord("Bob jr.", 23, 23000, "Doc");
p2 = PersonRecord("Martin jr.", 57, 36000, "King");
p3 = Manager("Rich sr.", 57, 36000);
p4 = PersonRecord("pippo", 100, 100, "Cartton");
records = [p1, p2, p3, p4]
print(p1)
print(p3)

print('Write classes to file')
with shelve.open('ClassShelve') as dbf:
    for x in records:
        dbf[x.name]=x

print('Read classes from file')
with shelve.open('ClassShelve') as dbf:
    for x in dbf.keys():
        print(dbf[x])
    Rich = dbf["Rich sr."]
    Rich.GiveRaise(0.1)
    dbf["Rich sr."] = Rich  #Notice how we still fetch, update, and reassign to keys to update the shelve
    print('------- More money to Rich sr. ---------')
    print(dbf["Rich sr."])
print('------------------------------------------------------------')

print('Read data in interactive way')

fieldnames = ('name', 'age', 'job', 'pay')
with shelve.open('ClassShelve') as dbf:
    while True:
        key = input('Key? ')
        if not key: break
        try:
            record = dbf[key]
        except: 
            print('Not Found')
        else:
            for f in fieldnames:
                print(f, ':' , getattr(record,f))

print('Stop reading data')



