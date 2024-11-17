import numpy as np
a = np.array ([[1,2,3,4,5,6,7],[8,9,10,11,121,13,14]])
#print(a)
#print(a[1,5]) # accessing a element
#print(a[1,-2]) #same element
#print(a[0,:]) #specific row
#print(a[:,2]) # specific column
#print(a[0,1:6:2]) # startindex:endindex(exclusive):stepsize
#a[1,5]=20 #changing a elements
#a[:,2]=5 #changed all to five
#a[:,2]=[1,2] #changes into 1,2
#print(a)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3d array
#print(b)
#print(b[0,1,1]) #getting a aspecific element,every other changes will work too
b[:,1,:] = [[9,9],[8,8]] #can be replaced as long as it is the same dimension
print(b)
