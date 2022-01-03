class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        return super().show()



    


a1 = B()
a1.show()
