# constructor, data member, methods are inherited
# private member and methods are not inherited to derived class
class Phone:
    def __init__(self, kernel, os, ram, storage):
        self.__kernel = kernel
        self.os = os
        self.ram = ram
        self.storage = storage

    def buy_phone(self):
        print("You bought a phone")

class SmartPhone(Phone):
    def __init__(self, kernel, os, ram, storage):
        super().__init__(kernel, os, ram, storage)
        print(self.os)

    # This is known as method overriding
    def buy_phone(self):
        print("You bought a smart phone")

redmi = SmartPhone('android', 4, 32, 2)
redmi.buy_phone()

nokia = Phone('keypad', 1, 4, 1)
nokia.buy_phone()

