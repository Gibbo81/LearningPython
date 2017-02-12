

import sys
import numpy


print(sys.__doc__)  #to read a description of an imported module we can access to __doc__
print('***************************************************************************')
print(numpy.__doc__)
print('***************************************************************************')
print(numpy.argpartition.__doc__) #worhs also on method
print('***************************************************************************')
help(numpy.polyder) #or simpler use help function
print('***************************************************************************')