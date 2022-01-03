class student:
    school="lpu"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.laptop()
    
    def show(self):
        print(self.name,self.age,self.school)
        self.lap.show()
        
    
    class laptop:

        def __init__(self):
            self.cpu='i5'
            self.ram=8
            self.hhd=1
        
        def show(self):
            print(self.cpu,self.ram,self.hhd)


std1=student('a',20)
std2=student('a1',21)
std1.show()