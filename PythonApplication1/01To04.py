def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

def StringTest():
    s='spam'
    print(s)
    print(s*2)
    print(s.replace('pa','yu'))
    msg="""
aaa
b'b'b
ccc"""
    print(msg)
    link=R'http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html'
    print(link)
    return;

def ListTest():
    l=[123,'spam spam',15.69]
    print(l)
    l=l+['add1']
    l.append('add2')
    print(l)
    l.pop(1)
    print(l)
    
    nesting=[[1,3],[7,9,5]]
    print('nesting: ' + str(nesting))
    print('nesting[1][0]: '+ str(nesting[1][0]))
    print('nesting[0][1]: '+ str(nesting[0][1]))
    return;

def ListComprehensionExpression():
    list=[[1,3,5],[7,9,5],[77,79,75]]
    print('list: ' + str(list))
    c=[row[1] for row in list]
    print('[row[1]for row in list]: ' + str(c))
    c=[row[0]*2 for row in list]
    print('[row[0]*2 for row in list]: ' + str(c))
    c=[row[2]*2 for row in list if row[2]>6]
    print('[row[2]*2 for row in list if row[2]>6]: ' + str(c))
    c=[list[i][i] for i in [0, 1, 2]]
    print('[list[i][i] for i in [0, 1, 2]]: '  + str(c))
    c=[d * 2 for d in 'spam']
    print('[d * 2 for d in \'spam\']: ' + str(c))
    c=[x**2 for x in range(8) if x%2==0]
    print('[x**2 for x in range(8) if x%2==0]: ' + str(c))

    print('create generators: (sum(row) for row in list)')
    gen=(sum(row) for row in list)
    print('next(gen): ' + str(next(gen)))
    print('next(gen): ' + str(next(gen)))
    print('next(gen): ' + str(next(gen)))
    return;

def Dictionaries():
    dit={'car':'focus','money':33,'decimal':98.357}
    print('dit: ' + str(dit))
    print('dit[\'money\']: ' + str(dit['money']))
    dit['money']=dit['money']+1
    print(dit)
    d={}            #Empty dictionary
    d['a']=12       #building little by little
    d['b']=24
    d['c']=64
    print('dinamically build: ' + str(d))
    b=dict(car='focus',money=33,decimal=98.357) #Different way to buil a dictionary with all the data
    print('\'plan\' in dit: ' + str('plain' in dit))
    print('To obtain a list of key')
    lkey = list(dit.keys())
    print(lkey)  #the order is not always the same
    lkey.sort()  #sort the collection
    print(lkey)
    for key in lkey:
        print(key, '=>', dit[key])          # key, '=>', dit[key] || ?na lista   
    return;

def ForLoop():   # In reality it's the foreach
    print('Testing the for loop')                           
    list =  [1,2,3,4,'r',6,7,8]
    print(list)
    for x in list:
        print(x)
    dictionary = {'a':2,'b':3,'ds':1233124,'uikj':'ttt'}
    print(dictionary)
    for x in dictionary:
        print(str(x) + " : " + str(dictionary[x]))
    for x in dictionary.values():
        print(x)
    print('works also on string \'Happy\'')
    s="Happy" 
    for x in s:
        print(x)
    return;

def MixingDictionariesAndList():
    mix={'name':{'first':'Giuliano','last':'Masi'},
         'jobs':['warrior','programmer'],
         'age':86}
    print(mix)
    print('mix[\'name\'][\'last\']: '+ str(mix['name']['last']))
    print('mix[\'jobs\'][0]: ' + str(mix['jobs'][0]))
    mix['jobs'].append('airman')
    print('Added a new job')
    print(mix)
    return;

def Tuple():        #Tuple are fixed immutable list
    t=(1,2,3,4,5)
    print(t)
    t=('err',1,4,[1,5,'uttf',8],{'a':1,'b':'yyy'})
    print(t)
    return;

def Files():
    print('writing on fles')
    fw=open('data.txt','w')         #make a new file in output ['w' write mode]
    writen = fw.write('Hello world\n....')
    fw.close()                        #close to flush output
    fr = open('data.txt')           #equal to  open('data.txt','r') that is the default
    readed = fr.read()  
    print('read from file: ' + readed)
    counter=1
    print('Read line at time')
    for line in open('AAA.txt'):
        print('line number ' + str(counter) + ' : ' + line) 
        counter=counter+1 
    print('Different encoding UTF8')
    s='sp\xc4m'
    print(s)
    fwu = open('dataUTF8.txt','w',encoding='utf-8')
    fwu.write(s)
    fwu.close()
    counter=1
    for line in open('dataUTF8.txt',encoding='utf-8'):
        print('Unicode line number ' + str(counter) + ' : ' + line) 
        counter=counter+1 
    return;

def SetCollection():        #are unorder colection of unique and immutable objects
    print('Working with SET')
    set = {'h','yyy', 3, 5.8}                 #similar to dictionary but without the key
    set.add(78)
    print (set)
    return;

#define a new class:
class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1 + percent)

def UseClassWorker():
    bob= Worker('Bob smith', 24000)
    sue = Worker('Sue Chan', 56700)
    print(bob.lastName())
    print(sue.lastName())
    bob.giveRaise(10)
    print(bob.pay)

printme("WAR")
print('Hello World')
print('------------------------------------------------------------')
StringTest()
print('------------------------------------------------------------')
ListTest() 
print('---------------------------------------------------------    ')
ListComprehensionExpression()
print('---------------------------------------------------------    ')
Dictionaries()
print('---------------------------------------------------------    ')
MixingDictionariesAndList()
print('---------------------------------------------------------    ')
ForLoop()
print('---------------------------------------------------------    ')
Tuple()
print('---------------------------------------------------------    ')
Files()
print('---------------------------------------------------------    ')
SetCollection()
print('---------------------------------------------------------    ')
UseClassWorker()
print('---------------------------------------------------------    ')

print('---------------------------------------------------------    ')
#input('Press Enter to Exit')  here is automatic!!!!!