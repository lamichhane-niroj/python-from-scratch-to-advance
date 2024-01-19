# There is no concept of method overloading in python but we can make our code to work it like
# The below code will not work in python
# class Geometry:
#
#     def area(self, length, breadth):
#         print("Area: ", length*breadth)
#
#     def area(self, radius):
#         print("Area: ", 3.14*radius**2)
#
#
# g1 = Geometry()
# g1.area(4, 5)
# g1.area(2)

class Geometry:
    @staticmethod
    def area(length, breadth=0):
        if breadth == 0:
            print("Area: ", 3.14*length**2)
        else:
            print("Area: ", length*breadth)


Geometry.area(5, 20)
Geometry.area(10)
