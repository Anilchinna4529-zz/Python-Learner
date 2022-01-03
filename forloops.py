from array import *
n=int(input("enter a"))
arr=array('i',[])
for i in range(n):
    y=int(input("Enter the element"))
    arr.append(y)
print(arr)
z=int(input("dell:"))
for e in arr:
    if e==z:
        arr[e-1]=arr[e]
        
    else:
        continue
print(arr)
