# If same method or variable is present in both parent and child class it overwrites

class A:
    def sayhello(self):
        print('Hello from class A')


class B(A):
    # This function overwrites the same function of class A
    def sayhello(self):
        print('Hello from Class B')


b_obj = B()
a_obj = A()

a_obj.sayhello()
b_obj.sayhello()  
