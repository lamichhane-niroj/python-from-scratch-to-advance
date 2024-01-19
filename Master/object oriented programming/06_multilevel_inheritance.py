#It is the level inheritance eg Grandparent parent and child

class Vehicle:
    def show_detail1(self):
        print('I am vehicles')

class Two_wheelers(Vehicle):
    def show_detail2(self):
        print('I am two wheelers')
    

class Bike(Two_wheelers):
    def show_detail3(self):
        print('I am bike')


suzuki = Bike()
suzuki.show_detail1()
suzuki.show_detail2()
suzuki.show_detail3()