#qn 1
import calendar
import datetime

class Time:
    def __init__(self):
        self.showoption()

    def showoption(self):
        print('''
        1. calender
        2. Time
        3. Date
            ''')

        choice = int(input('Enter your choice:'))

        if choice==1:
            self.calendar()
        elif choice==2:
            self.time()
        elif choice==3:
            self.date()
        else:
            print('Invalid input')

    def calendar(self):
        yr = int(input('Enter year:'))
        mn = int(input('Enter month:'))

        print(calendar.month(yr,mn))
    

    def time(self):
        print('Time:',datetime.datetime.now().time())

    def date(self):
        print('Date:',datetime.datetime.now().date())

t1 = Time()


#qn 2
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


#qn 3
class Library:
    def __init__(self):
        self.books = ['mathematics I','electronics','applied physics','data structure','drawing','c++','python','microprocessor','thermodynamics']
        self.userid = 'PUR077BCT052'
        self.userpw = '1234'
        self.login()


    def login(self):
        id = input('Enter user id:')
        pw = input('Enter your password:')

        if id==self.userid and pw ==self.userpw:
            print('Login succesfully')
            self.options()
        
    def options(self):
        while True:
            print('''
                1. Request a book
                2. Return a book
                3. Show books
            ''')

            choice = int(input('Enter your choice:'))

            if choice==1:
                self.request_book()
            elif choice==2:
                self.return_book()
            elif choice==3:
                self.show_books()
            else:
                print('Invalid input')
                break


    def request_book(self):
        temp = input('Enter book name')
        temp = temp.lower()

        if temp not in self.books:
            print('Sorry, the book is not available at the moment')
        else:
            print('You have received the book')
            self.books.remove(temp)


    def return_book(self):
        temp = input('Enter book name')
        temp = temp.lower()

        self.books.append(temp)


    def show_books(self):
        print('Available books are:\n')
        for book in self.books:
            print(book)


l1 = Library()