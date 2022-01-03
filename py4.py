class student:
    
    def __init__(self,name,rolln):
        self.name = name
        self.rolln = rolln
        self.lap = self.laptop()

    def show(self):
        print(self.name , self.rolln)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand  = "hp"
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

    
s1 =student("anil",2)
s2 = student("jj",3)

s1.show()
s2.show()
#print(s1.show())