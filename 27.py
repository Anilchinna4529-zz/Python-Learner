from array import *

l=array('i',[])
n=int(input("value : "))
for i in range(n):
    x=int(input("elemnets: "))
    l.append(x)
print(l)

val=int(input("del: "))
k=0

for e in (0,n-1):
    if e==val:
        l.pop(e+1)
        break
    k+=1
print(l)

        