print('Modules are imported only one time')
import importing.PrintOnImport
print('if we run the iport again nothing happen')
import importing.PrintOnImport
#there is no link from a name copied with from back to the file it came from. To really change a global name in
#another file, you must use import:  import small; small.x = 42 # Changes x in other module
#from only copy names from one module to another

print("list(importing.PrintOnImport.__dict__.keys()) : ",list(importing.PrintOnImport.__dict__.keys()));
userdefinedlist=[name for name in importing.PrintOnImport.__dict__.keys() if not name.startswith('__')]
print("Print only name define in the code: ",userdefinedlist)