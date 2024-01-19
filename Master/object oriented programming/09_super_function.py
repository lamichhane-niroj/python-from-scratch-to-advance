# Super method is used to initialize the parent method
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


sq = Square(5,5)
cu = Cube(5,2,3)

print(sq.area(), cu.volume())
