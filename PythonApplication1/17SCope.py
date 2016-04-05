x=13    #this variable is global
globvar = 0
import importing.ImportVariable as ImportVariable 

def GlobalVarPrint():
    print("global variable globvar: ", globvar)
    print("global variable x: ",x)
    return

def GlobalVarChange():
    global globvar  #if we declare this variable ad global the next assigment reference the global one
    globvar="globale"   #instead of working creating a new local variable that hie the global one
    GlobalVarPrint()
    return

def LocalOverride():
    x='23232'   #this is a local assignment it create a new x local variable not change the global one
    print("Changed x into: ",x)

def ChangeRet():
    x='23232'   
    print("Changed x into: ",x, ' and return it back')
    return x    #to really change an mmutable type we need to pass it back

def TestChangeExternalModuleVariables(): #We can change variable from another files 
    print('change original value')       #but it's a bad practice
    ImportVariable.PrintmyList()
    ImportVariable.lis.append("pippo")
    ImportVariable.PrintMyNumber()
    ImportVariable.num=45
    return

def CreateNewGlobalVariable():
    print('Create 2 new global variables new1 and new2')
    global new1
    global new2
    new1=int(x)+25
    new2="lotto alle otto"
    
def NonLocalVariable(): #use of command nonlocal
    nl=12               #similar to global but it's referred only to the enclosing visibility scope
    print("nl: ", nl)
    def Internal(u):
        print('Change a variabale of the enclosing local scope to ',u)
        nonlocal nl
        nl=u
    Internal("new value")
    print("nl: ", nl)

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
ImportVariable.PrintmyList()
ImportVariable.PrintMyNumber()
print('-----------------------------------------------------------------')
CreateNewGlobalVariable()
print('new1: ',new1)
print("new2: ",new2)
print('-----------------------------------------------------------------')
NonLocalVariable()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')