print('Importing Changer')
X=100
print("Done x:100")
print("printing variable __name__:", __name__)

#We can create a sort a unit test that do not run when we are importing the module!!!!!
if __name__=='__main__':                        
    print("used as main for the program")
else:
    print("imported as module")





