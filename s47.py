def add():
    print("call only add",__name__)
def sub():
    print("call only sub")
def main():
    add()
    sub()

if __name__=="__main__":
    main()