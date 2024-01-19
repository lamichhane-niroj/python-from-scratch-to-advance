#if child class inherit the property of two or more parent class, eg:mother,father and child

class Mammals:
    def property1(self):
        print('I am mammal')

class Winged_animals:
    def property2(self):
        print('I have wings')

class Bat(Mammals,Winged_animals):
    pass

bat = Bat()
bat.property1()
bat.property2()
