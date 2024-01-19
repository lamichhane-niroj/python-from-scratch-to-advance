# operator overloading is an example of polymorphism
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self,f2):
        tempnum = self.num * f2.den + self.den * f2.num
        tempden = self.den * f2.den
        return f'{tempnum}/{tempden}'

    def __sub__(self,f2):
        tempnum = self.num * f2.den - self.den * f2.num
        tempden = self.den * f2.den
        return f'{tempnum}/{tempden}'

    def __mul__(self,f2):
        tempnum = self.num * f2.num
        tempden = self.den * f2.den
        return f'{tempnum}/{tempden}'

    def __truediv__(self,f2):
        tempnum = self.num * f2.den
        tempden = self.den * f2.num
        return f'{tempnum}/{tempden}'

f1 = Fraction(1,2)
print(f1)

f2 = Fraction(2,3)
print(f2)

print(f1+f2)
print(f1-f2)
print(f1/f2)
print(f1*f2)

