import sys
import ctypes

a = [1,2,3]
c = b = a
#ctypes.c_long.from_address(address).value
print(id(a)) #address of list a
print(sys.getrefcount(a)-1) # number of references pointing to address of a
