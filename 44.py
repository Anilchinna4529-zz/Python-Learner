def sum(a,b):
    print(a/b)
    return
    

def dec_sum(sum):
    def inner_assign(a,b):
        if a<b:
            a,b=b,a
        return sum(a,b)
    return inner_assign

sum=dec_sum(sum)
sum(2,4)
