class Student():
    #constructor
    def __init__(self):
        self.name = input("Enter your name: ")
        self.faculty = input("Enter your faculty: ")
        self.rollno = input("Enter your rollno: ")
        print("")

    #detail of student
    def show_detail(self):
        print("Student Details:")
        print("Name = ", self.name)
        print("Faculty = ", self.faculty)
        print("Rollno = ", self.rollno)
        print("")
    
    #requested book of student
    def requestbook(self):
        print("Enter the name of the book you would like to check out: ")
        self.book = input()
        return self.book

    #book return by student
    def return_book(self):
        print("The book you want to return is: ")
        self.retbook = input()
        return self.retbook

class Library():
    #constructor
    def __init__(self, listofbook):
        self.listofbook = listofbook
    
    #displaying books
    def displaybook(self):
        print("The available books in our library are: ")
        for book in self.listofbook:
            print(book)
        print("")
    
    #lending book to student
    def lend_book(self, reqbook):
        if reqbook in self.listofbook:
            print("You have borrowed the book")
            self.listofbook.remove(reqbook)
        else:
            print("Sorry, it's not available in the library")
        
    #updating book
    def update_book(self, book):
        self.listofbook.append(book)

library = Library(["Rich dad poor dad", "The richest man in the babylon", "Harry potter"])
student = Student()    
done = True

while done:
    print('''====LIBRARY MENU====
          1. Display all available books
          2. Show my details
          3. Request a book
          4. Return a book
          5. Exit
    ''')
    choice = int(input("Enter Choice: "))
    if choice == 1:
        library.displaybook()
    elif choice == 2:
        student.show_detail()
    elif choice == 3:
        library.lend_book(student.requestbook().capitalize())
    elif choice == 4:
        library.update_book(student.return_book())
    else:
        done = False




