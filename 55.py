class A():

    def __init__(self):
        print("A init fun")

    def feature1(self):
        print("feature1 fun")
    def feature2(self):
        print("featur2 fun")
class B(A):

    def __init__(self):
        super().__init__()
        print("B init fun")
        
    def feature3(self):
        print("feature3 fun")
    def feature4(self):
        print("featur4 fun")

class C(A,B):
    pass
    def __init__(self):
        super().__init__()
        print("C init fun")
c1=C()
c1.feature1()