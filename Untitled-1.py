a=200
d=5000
for k in range(1,d+1):
    while (a<=((k//2)+1)):
        if a**2==k:
            print(k)
        a=a+1
    a=200