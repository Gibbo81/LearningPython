class SearchingTest:     
    def __init__(self, value):
        self.Data=value
    def __add__(self, other):
        return SearchingTest(self.Data + other)



a= SearchingTest(10)
#a.__add__= lambda x: self.Data + x     #this is not working 
                                        #we are searching for __add__ inside the class not the istance!!!
b= a+12
print(b.Data)

