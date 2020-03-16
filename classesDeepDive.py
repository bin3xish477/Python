'''
Alexis Rodriguez
7 July 2019
Python:
- getters and setters
- magic methods (modifyies built-in functions)
'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    #redefining properties of class
    @property #getter
    def width(self):
        return self._width
    @width.setter #setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Cannot be 0 or less than 0")
        else:
            self._width = width
    @property #getter
    def height(self):
        return self._height

    @height.setter #setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Cannot be 0 or less than 0")
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other): #rewriting build-in system methods
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __repr__(self): #rewriting build-in system methods
        return f"Rectangle({self.width}, {self.height})"

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(20, 30)

print(r1)
print(r2)
print(r3)
print()
print(r1 == r2)
print(r1 == r3)
print(r2 == 100)
print()
print(r1 < r3)
print(r1 < r2)
print()
print(r1 > r3)
print(r1 > r2)
print()
print(r1.width)
print(r2.height)
r3.width = 100
print(r3)
r2.height = 100
print(r2)
#exception
r1.width = -10
