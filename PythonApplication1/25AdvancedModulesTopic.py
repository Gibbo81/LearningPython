import sys

def TestingCommandLineParameter():
    if len(sys.argv)==1 :
        print('No arguments from command line')
    else:
        print("Printing all command argument")
        for x in sys.argv[1:]:                      #the first parameter is always the name of the script
            print(x, end=' ')
        print("")




print('-----------------------------------------------------------------')
print("printing variable __name__:", __name__)
print('But this variable has a different name if used in a different contest:')
import importing.Changer    
print('in an imported module __name__ is the name of the file: importing.Changer')
print('-----------------------------------------------------------------')
TestingCommandLineParameter()
print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')

print('-----------------------------------------------------------------')


