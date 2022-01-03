books=["anabelli","gost","tutor","smile","love story","bottle","premum","movie","boy","the leader"]
s=[]
for i in books:
    if i.startswith("b"):
        s.append(i)
#print(s)

s=[j for j in books if j.startswith("b")]
print(s)