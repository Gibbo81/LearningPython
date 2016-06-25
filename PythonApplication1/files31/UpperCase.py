if __name__ == '__main__':  #it take the relative position from the master!!!!!! in this case 31DesigningWithClasses.py
    import Processor as p
else:
    import files31.Processor as p 
import sys
#to avoid this problem it will be batter to have a directory for all the file to do not have problem

class UpperCase(p.Processor):
    def Converter(self, data):
        return data.upper()

if __name__ == '__main__':
    worker = UpperCase(open('.\\files31\\Righe.txt',"r"), sys.stdout)   #but the file still need to be called with \\files31
    worker.process()
    print()
    import os
    print(os.getcwd())      #as you can see from the current directory
