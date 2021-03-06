﻿from imp import reload

print('Modules are imported only one time')
import importing.PrintOnImport
print('if we run the iport again nothing happen')
import importing.PrintOnImport
#there is no link from a name copied with from back to the file it came from. To really change a global name in
#another file, you must use import:  import small; small.x = 42 # Changes x in other module
#FROM only copy names from one module to another, we get copies of those names not links to them

print("FROM only copy names from one module to another, we get copies of those names not links to them")
print('-----------------------------------------------------------------')
print("list(importing.PrintOnImport.__dict__.keys()) : ",list(importing.PrintOnImport.__dict__.keys()));    #__dict__ dictionary with all the attributeof a module
userdefinedlist=[name for name in importing.PrintOnImport.__dict__.keys() if not name.startswith('__')]
print("Print only name define in the code: ",userdefinedlist)
print('-----------------------------------------------------------------')
#Reload give the way to reimport a module
#Reload impacts all clients that use import to fetch modules. 
#Reload impacts future from clients only. Clients that used from to fetch attributes in the past won’t be 
#affected by a reload; they’ll still have references to the old objects fetched before the reload.
#This because thay have made a copy of the reference to the object so they still point to the old one
from importing.Changer import X
import importing.Changer
print("import a module in both the way")
print("X: ",X)
print("importing.Changer.X: ",importing.Changer.X)
print("Now change both X!!!!")
X+=50
importing.Changer.X+=60
print("X: ",X)
print("importing.Changer.X: ",importing.Changer.X)
print("-----------Reload the module----------")
reload(importing.Changer)
print("-----------Reloaded ------------------")
print("from does not change X: ",X)
print("import goes back to original value importing.Changer.X: ",importing.Changer.X)
print('-----------------------------------------------------------------')