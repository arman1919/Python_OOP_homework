from abc import ABC, abstractmethod

class Shape(ABC):   
    @abstractmethod
    def __area__(self):
        pass


class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
        super().__init__()
    def __area__(self):

        return 3.14*2*self.radius


class Rectangle(Shape):
    def __init__(self,side) -> None:
        self.side = side

    def __area__(self):

        return self.side**2


cir = Circle(12)

rec = Rectangle(5)


print(cir.__area__())

print(rec.__area__())



