x=100
while x<100:

    if x%3==0:
        if x%5==0:
            print("ding dong")
            
        else:
            
            print("ding")
            continue
    elif x%5==0:
        print("dang")
    else:
        print(x)
x=x+1
