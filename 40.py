import sys
sys.getrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def g():
    global i
    i+=1
    print("hi")
    g()

g()