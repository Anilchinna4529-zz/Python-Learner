from array import *
val=int(input("enter the number"))
arr=array('i',[])
for e in range(0,val):
    m=int(input("enter the element"))
    arr.append(m)
print(arr)
#k=0
for i in range(int(val/2)):
    k=arr[i]
    arr[i]=arr[val-i-1]
    print(arr)
    arr[val-i-1]=k
print(arr)