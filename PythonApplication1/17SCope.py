x=13    #this variable is global
globvar = 0
import importing.ImportVariable as ImportVariable 

def GlobalVar():
    print("global variable globvar: ", globvar)
    print("global variable x: ",x)
    return

def GlobalVarChange():
    global globvar  #if we declare this variable ad global the next assigment reference the global one
    globvar="globale"   #instead of working creating a new local variable that hie the global one
    GlobalVar()
    return

def Change():
    x='23232'   #this is a local assignment it create a new x local variable not change the global one
    print("Changed x into: ",x)

def ChangeRet():
    x='23232'   
    print("Changed x into: ",x, ' and return it back')
    return x    #to really change an mmutable type we need to pass it back

def TestChangeGlobalVariable():
    print('change origina value')
    ImportVariable.PrintmyList()
    ImportVariable.lis.append("pippo")
    ImportVariable.PrintMyNumber()
    ImportVariable.num=45
    return


print("testing the LEGB local-enclosing-global-built in")
GlobalVar()
print('-----------------------------------------------------------------')
GlobalVarChange()
print('-----------------------------------------------------------------')
print(x)
Change()
print(x)
x=ChangeRet()  # this go on the global war
print(x)
print('-----------------------------------------------------------------')
TestChangeGlobalVariable()
print('-----------------------------------------------------------------')
print("Both this actions had changed our variable in a global way, also the nuber that is animmutable type")
ImportVariable.PrintmyList()
ImportVariable.PrintMyNumber()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')
