# inheritance
class Person:
    # constuctor
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def details(self):
        print(f"I am {self.name}. I am {self.age} years old and i am {self.weight} kgs", end=" ")


class Student(Person):
    # constuctor
    def __init__(self, name, age, weight, grade, roll):
        super().__init__(name, age, weight)
        self.grade = grade
        self.roll = roll


    def details(self):
        super(Student, self).details()
        print(f"i study in {self.grade} class and my roll number is {self.roll}")


class Teacher(Person):
    # constuctor
    def __init__(self, name, age, weight, idno):
        super().__init__(name, age, weight)
        self.idno = idno


    def details(self):
        super(Teacher, self).details()
        print(f"and my id number is {self.idno}")


if __name__ == "__main__":
    ronal = Student(name="Ronal", weight=70, age=22, grade=12, roll=54)
    ram = Teacher(name="Ram", weight=80, age=45, idno=4598)

    ronal.details()
    ram.details()

























# Object are the instances of class, object has data attributes and methods attributes, In large scale code oop is very useful in writing codes and maintains readability
"""
# class are the blueprint for the object, objects are the instances of the class
# Everything in python is an object of its class for example
print(type([1,2,3]))    # it's of list class
print(type(1))          # it's of int class
print(type(1+2j))       # it's of complex class

num = 1+2j
print(num.real)         # it is data attribute
print(num.imag)         # it is data attribute
print(num.conjugate())  # it is method attribute

# creating simple class
class Hello():
    # simple method attribute
    def say_hello(self):
        print("Hello world")
    
    def say_hi():
        print('Hi world')


# object of class Hello
h1 = Hello()
# Accessing its method attributes
Hello.say_hello(h1)

# h1.say_hi()  # typeerror: Hello.say_hi() takes 0 positional arguments but 1 was given, therefore it internally passes something
                # which is it itself so we write self
          

class Student_record():
    def initialize(self, name, rollno, faculty):
        self.name = name
        self.rollno = rollno
        self.faculty = faculty
    
    def show(self):
        print(f'''Name = {self.name}
Rollno = {self.rollno}
Faculty = {self.faculty}
        ''')


s1 = Student_record()
s2 = Student_record()

s1.initialize('Niroj','PUR077BCT052','Computer')
s2.initialize('Manoj','PUR077BCT045','Computer')

print(s1.name)          # accesing data attribute
Student_record.show(s1) # accesing by passing object as an argument
s2.show()               # accessing by object as caller

"""















  
