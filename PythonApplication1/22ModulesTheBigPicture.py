import sys
import importing.FuncTest as ooo

def PrintImportedLib():
    print("Print all current imported modules")
    res=list(sys.modules.keys())
    res.sort()
    for x in res:
        print(x)

def PrintImportFilesPathList():
    print('Print the modules serch path on my platform')
    for x in sys.path:
        print(x)
        
print('-----------------------------------------------------------------')
PrintImportedLib()
print('-----------------------------------------------------------------')
PrintImportFilesPathList()
print('-----------------------------------------------------------------')






