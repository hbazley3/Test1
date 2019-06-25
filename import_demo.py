# Use separte namespaces for "math" module
print('List of object names in _main_ namespace: ')
print(dir())
import math
print('List of object names in _main_ namespace' , end=' ')
print('after "import math" has excuted:')
print(dir())
print('The value of pi is ', math.pi)
print ('The tangent of 1 is ' , math.tan(1))
del(math)

# Use separte aliased namespaces for "math" module
print('List of object names in _main_ namespace: ')
print(dir())
import math as fun
print('List of object names in _main_ namespace' , end=' ')
print('after "import math as fun" has excuted:')
print(dir())
print('The value of pi is ', fun.pi)
print ('The tangent of 1 is ' , fun.tan(1))
del(fun)

# Import selectively into _main_ namespace
print('List of object names in _main_ namespace: ')
print(dir())
from math import pi, tan
print('List of object names in _main_ namespace' , end=' ')
print('after "import from math import pi, tan" has excuted:')
print(dir())
print('The value of pi is ', pi)
print ('The tangent of 1 is ' , tan(1))
del(pi)
