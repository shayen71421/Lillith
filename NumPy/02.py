import numpy as np
a = np.array([1,2,3])# 1d array
#print(a)
b = np.array([[9.1,8.0,7.0],[6.0,5.0,4.0]]) # 2d array
#print(b)
#print(a.ndim) # tells the dimension of the array
#print(b.ndim)
#print(b.shape)# shows the row x col
#print(a.dtype) # shows the way it is stored
#print(b.dtype)
c = np.array([1,2,3],dtype='int16') #is now made ot store into a sepcific data type
#print(c.dtype)
#print(c.itemsize) # shwos the size in bytes
#print(c.size) # total n of elememts
print(a.nbytes) #shows total bytes used which is itemsize x size