class A:

    def __init__(self):
        print("in it A function")
    def feature1(self):
        print("these feature1 is working well : ")
    
    def feature2(self):
        print("these feature2 is working well : ")
    
class B:
    def __init__(self):
        print("in in B")
    def feature3(self):
        print("these feature3 is working well : ")
    
    def feature4(self):
        print("these feature4 is working well : ")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in it C")
        
    def feat(self):
        super().feature1()
   

a1=C()
a1.feat()
