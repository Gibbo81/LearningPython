x=13    #this variable is global
globvar = 0
import importing.ImportVariable as ImportVar 

def GlobalVarPrint():
    print("global variable globvar: ", globvar)
    print("global variable x: ",x)
    return

def GlobalVarChange():
    global globvar      #if we declare this variable ad global the next assigment reference the global one
    globvar="globale"   #instead of creating a new local variable that hit the global one
    GlobalVarPrint()    #global declaration make the search begin in the global scope LEGB (start from G) 
    return

def LocalOverride():
    x='23232'   #this is a local assignment it create a new x local variable not change the global one
    print("Changed x into: ",x)

def ChangeRet():
    x='23232'   
    print("Changed x into: ",x, ' and return it back')
    return x    #to really change an immutable type we need to pass it back

def TestChangeExternalModuleVariables(): #We can change variable from another files 
    print('change original value')       #but it's a bad practice!
    ImportVar.PrintmyList()
    ImportVar.lis.append("pippo")
    ImportVar.PrintMyNumber()
    ImportVar.num=45
    return

def CreateNewGlobalVariable():  #Global variable must not already be defined when we use 'global new1'
    print('Create 2 new global variables new1 and new2')
    global new1
    global new2
    new1=int(x)+25              #here we define 2 new globalvariable for this file
    new2="lotto alle otto"
    
def NonLocalVariable(): #use of command nonlocal
    nl=12               #similar to global but it's referred only to the enclosing visibility scope
    print("nl: ", nl)   #and variable must always be already defined when we declare them as nonlocal
    def Internal(u):
        print('Change a variabale of the enclosing local scope to ',u)
        nonlocal nl
        nl=u
    Internal("new value")
    print("nl: ", nl)

def FunctionFactory(n=7):       #lambda is always a single expression, it cann't spam on more lines
    return lambda x: x**n       # function are object and can be assigned or return as normal value
    # action = lambda x: x**n   #would be also a valid way to obtain the same result
    # return action
    # def action(x):             #this can be a third way to do the same thing
    #   return x**n
    # return action

def ManteiningStateBetweenExecution(starting):
    def internalfunc(label): 
        nonlocal starting       #in this way the function now has its own state
        print(label,starting)   #starting value is keeped and incremented ad each new use
        starting+=1             #of this function
    return internalfunc

def UsingFunctionAttribute(starting):   #function can have attribute associated with them as
    def internalfunc(label):            #internalfunc.counter. but they must be initialized
        print(label,internalfunc.counter)
        internalfunc.counter+=1
    internalfunc.counter=starting       #manually after the function definition
    return internalfunc

print("testing the LEGB local-enclosing-global-built in")
GlobalVarPrint()
print('-----------------------------------------------------------------')
GlobalVarChange()
print('-----------------------------------------------------------------')
print(x)
LocalOverride()
print(x)
x=ChangeRet()  # this go on the global war
print(x)
print('-----------------------------------------------------------------')
TestChangeExternalModuleVariables()
print("Both this actions had changed our variable in a global way, also the number that is an immutable type")
ImportVar.PrintmyList()
ImportVar.PrintMyNumber()
print('-----------------------------------------------------------------')
CreateNewGlobalVariable()
print('new1: ',new1)
print("new2: ",new2)
print('-----------------------------------------------------------------')
NonLocalVariable()
print('-----------------------------------------------------------------')
print("Using function factory")
f1=FunctionFactory(4)
f2=FunctionFactory(10)  #different function with with its own set of state information
f3=FunctionFactory()
print(f1(3))
print(f2(3))
print(f3(3))
print('-----------------------------------------------------------------')
print("Manteining function state between execution")
func1=ManteiningStateBetweenExecution(21)
func1('a')
func1('b')
func1('c')
print('-----------------------------------------------------------------')
print("Using function attribute to obtain the same result")
f1=UsingFunctionAttribute(10)
f2=UsingFunctionAttribute(200)
print('f1.counter ',f1.counter)
print('f2.counter ',f2.counter)
f1("halo")
f2('two')
f1(r"halo 2:")
f2(r'two 2:')
print('-----------------------------------------------------------------')