from numpy import *
arr=array([ [1,2,3,4,5],
            [2,3,9,5,6],
            [2,3,4,5,6]

            ])
print("dimension",arr.ndim)
print("data type",arr.dtype)
print("shape",arr.shape)
arr1=arr.flatten()
print(arr1)
m=matrix(arr1)
print(m)
print(m.min())
print(m.max())
arr2=array([1,2,3,4,6,7,8,9,10,11,12,13,14,15,16])
m1=arr1*arr2
print(m1)