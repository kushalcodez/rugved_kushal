from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c):
        self.color = c
    
    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    
    def get_area(self) -> float:
        return self.side * self.side

#driver
color = input("Enter color: ")
side = float(input("Enter side: "))

square = Square(color, side)
print(f"Color: {square.get_color()}")
print(f"Area: {square.get_area()}")

try:
    shape = Shape("blue")
except TypeError as e:
    print(f"Cannot create Shape: {e}")