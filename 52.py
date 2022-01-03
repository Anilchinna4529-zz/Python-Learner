class car:
    wheel=4
    def __init__(self) -> None:
        pass
        self.car='BMW'
        self.mil=20
c1=car()
c2=car()
c1.mil=21
print(c1.car,c1.mil,c1.wheel)
print(c2.car,c2.mil,c2.wheel)