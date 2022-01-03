def fat(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return x
        
y=4
result=fat(y)

print(result)