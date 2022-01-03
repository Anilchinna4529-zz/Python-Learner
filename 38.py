def feb(lst):
    a=0
    b=1
    for i in range(2,lst):
        c=a+b
        a=b
        b=c

        print(c)
feb(10)