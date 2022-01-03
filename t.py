for i in range(1,100):
    if i%3==0:
        if i%5==0:
            i="ding dong"
            print(i)
        else:
            i="ding"
            print(i)
            continue
    elif i%5==0:
        i="dang"
    else:
        print(i)

    
        