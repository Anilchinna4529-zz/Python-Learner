from typing import AsyncGenerator


class object:
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def person(self,name,age):
        name=input("Enter the name:")
        age=int(input("Enter the age:"))

    @classmethod   
    def compare(self,age,other):
        if self.age==other.age:
            return True
        else:
            return False
obj1=object()
obj2=object()


if obj1.compare(obj2):
    print("They are same ")
else:
    print("They are not same")


obj1.person()
obj2.person()
