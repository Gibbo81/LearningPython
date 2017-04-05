import InitialData as ID

bob = ['bob smith', 42, 30000,'software']
sue = ['sue Jones', 52, 50000,'hardware']

peoples = [bob, sue]
peoples.append(['tom boldo', 25, 31000,'farmer'])


print(peoples[0][0].split()[-1])
peoples[1][2] *= 1.25

for x in peoples:
    print(x)

#To 0obtain all the pays:
pays = [x[2] for x in peoples]
pays2 = map(lambda x : x[2] , peoples)
print(list(pays2))
print(pays)

bob = {'name': 'bob smith', 'age':42, 'pay': 3000, 'job': 'software'}
sue = {'name': 'sue Jones', 'age':52, 'pay': 5000, 'job': 'hardware'}
peoples = [bob, sue]
x= bob['name'], sue['age']  #tuple

print('------------------------------------------------------------')

print(ID.db)