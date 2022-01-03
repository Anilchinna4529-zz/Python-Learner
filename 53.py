class student():
    school = "LPU"
    def __init__(self,s1,s2,s3,s4):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4

    def avg(self):
        return(self.s1+self.s2+self.s3+self.s4)/4

    @classmethod
    def get_scl(value):
        return value.school

    @staticmethod
    def info():
        print("this is the static variable")

std1=student(44,54,6,8)
std2=student(85,9,66,88)\

print(std1.avg())

print(std2.avg())

print(student.get_scl())
student.info()