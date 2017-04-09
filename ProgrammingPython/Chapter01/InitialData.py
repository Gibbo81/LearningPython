
def GiveDb():
    bob = {'name': 'Bob Smith', 'age':31, 'pay': 45000, 'job':'dev'}
    sue = {'name': 'Sue Jones', 'age':25, 'pay': 49000, 'job':'SBA'}
    red = {'name': 'Red Green', 'age':83, 'pay': 0, 'job':None}

    db = {}
    db['bob'] = bob
    db['sue'] = sue
    db['red'] = red
    return db

if __name__ == '__main__':
    for key in db.keys():
        print("for key %s => %s" %(key,db[key]))
        

