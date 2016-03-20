def TestingWhileLoop():
    while True:
        reply = input('read a line: ')
        if reply=="": break             #break it's a single line so i can not to go to a new line
        print(reply.upper())
    
    while True:
        reply=input("Give me a number to elaborate : ")
        if reply=="": break
        elif reply.isdigit():             #check if a string {our input} is a valid int number
            print(int(reply)**2)
        else:
            print("Error " + reply + " is not a number")           
    print("bye")
    return;

def TryAndCatch():
    print("Using try/except")
    while True:
        reply=input("Give me a number to elaborate : ")
        if reply=="": break
        try:        
            print(float(reply)**2)
        except:
            print("Error " + reply + " is not a number")         
        finally:
            print("done")
    return;




TestingWhileLoop()
print('------------------------------------------------------------')
TryAndCatch()
print('------------------------------------------------------------')