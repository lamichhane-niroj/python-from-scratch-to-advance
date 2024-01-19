#parent class: User class contains user information
class User():
    def __init__(self, name, age, gender):
        print("The account has been created :)")
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_detail(self):
        print("\nPersonal Details:")
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Gender = ", self.gender)

#child class: Bank class contain bank information
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated to $",self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance -= self.amount
            print("Withdraw amount of $",self.amount)
        else:
            print("Sorry! Insufficient Balance | Balance Available = $", self.balance)  
    
    def view_balance(self):
        self.show_detail()
        print("Account balance has been updated to $",self.balance)
    

name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender(m/f): ")

user = Bank(name, age, gender)
dp = int(input("Enter the amount to be deposited: "))
user.deposit(dp)
wd = int(input("Enter the amount to be Withdrawn: "))
user.withdraw(wd)
user.view_balance()



