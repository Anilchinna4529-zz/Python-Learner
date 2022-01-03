class student:
    	
	school = "wisdom"

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2= m2
		self.m3 = m3

	def avg(self):
    		return(self.m1+self.m2+self.m3)/3
	def get_m1(self):
    		return self.m1
		
	def set_m2(self,values):
    		self.m2 = values
	@classmethod
	def get_class(cls):
    		return cls.school

	@staticmethod
	def info():
		print("these is staticmethod class")

s1 = student(34,44,55)
s2 = student(6,77,88)

print(s1.avg(),s2.avg())
print(student.get_class())
student.info()