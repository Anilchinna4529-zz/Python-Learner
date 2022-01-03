#from functools import map
from functools import reduce


ages = [1,2,3,4,5,6,7,8,9]
#using lamda function and filter
even=list(filter(lambda a: a%2==0,ages))
print(even)

#FILTER FUNCTION
#using bu def fun and filter
def even1(n):
    return n%2==0

result=list(filter(even1,ages))
print(result)

#MAPFUNCTION
#using def fun and map
def update(a):
    return a*2
doubles=list(map(update,result))
print(doubles)

#usnig lamda fun and map
add=list(map(lambda a:a*2,result))
print(add)

#REDUCE FUNCTION
#using def fun and reduce

a=[1,2,3,4,5]
b=[1,2,3,4,5]
sum=reduce(update,a)
print(sum)

#using lamda fun and reduce
sum2=reduce(lambda a,b:a+b,a)
print(sum2)