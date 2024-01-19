#Abstract class are those class which object cannot be made

from abc import ABC,abstractmethod


class Person(ABC):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @abstractmethod
    def show_info(self):
        print(self.name, self.age, self.sex, end=" ")


class Teacher(Person):
    def __init__(self,name, age, sex, salary):
        super().__init__(name, age, sex)
        self.salary = salary
        
    def show_info(self):
        super(Teacher, self).show_info()
        print(self.salary)


class Student(Person):
    def __init__(self,name, age, sex, rollno):
        super().__init__(name, age, sex)
        self.rollno = rollno
        
    def show_info(self):
        super(Student, self).show_info()
        print(self.rollno)


teacher = Teacher('Ram', 28, 'm', 45000)
teacher.show_info()

student = Student('Anish', 21, 'm', 21)
student.show_info()



