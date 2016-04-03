import importing.FuncTest as FuncTest   #in this way i can iport the file and also set a good name


FuncTest.PrintValue("print this variable")
print('-----------------------------------------------------------------')
#creatng a function it's only an assignmente to a variable done a runtime of a function object
#the name of a functin it's not different and is assigned a runtime whene we execute def statement
#we can assignment a function to any different variable a run time
variable= FuncTest.PrintValue
variable([1,2,3,4,8,9,70])
variable(variable)
print('-----------------------------------------------------------------')
lista=[1,2,3,4,5,6,7,8,9,0]
setb={1,3,67,6,9,0,14,99}
print(FuncTest.Intersect(lista,setb))
print(FuncTest.Intersect("war e war","there is only war"))
print('-----------------------------------------------------------------')
print("A function that call return without an argument return the default None")
print(FuncTest.NoneReturning())
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')