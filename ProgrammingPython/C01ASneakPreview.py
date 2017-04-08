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

print("Save eusing shalve")

SaveWithShelve('pepleshelve', ID.GiveDb())

with shelve.open('pepleshelve') as sf:
    red = sf['red']
    red['pay']=89
    sf['red'] = red     #we always need to change the hightest level inside shelve db
    listr = [value for value in  sf.values()]
    dictr = {key:sf[key] for key in sf.keys()}
    
print('list: %s' % listr)
print('dict: %s' % dictr)