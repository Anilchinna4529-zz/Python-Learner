class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
       
        print("computer config is cpu,ram",self.cpu,self.ram)
com1=computer('i5',26)

com1.config()

