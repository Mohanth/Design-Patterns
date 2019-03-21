"""

-- It's One of the creational pattern, which is used to create an object.
-- In Factory pattern, we create object without exposing the creation logic to the client.

Steps :
    1. Create an Interface
    2. Create Concrete class implementing the same interface
    3. Create a Factory to generate object of concrete class based on given information
"""


# Interface
class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class Rectangle(ShapeInterface):
    def draw(self):
        print("Rectangle.draw")


# Factory class
class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        elif type == 'square':
            return Square()
        elif type == 'rectangle':
            return Rectangle()


# s = ShapeFactory()
# s.getShape('rectangle').draw()

