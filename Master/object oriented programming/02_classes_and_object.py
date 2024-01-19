# ATM program using oop

class Atm:
    def __init__(self):
        self.balance = 100000
        self.info()
       
    
    def info(self):
        while True:
            print('''\n\n----Welcome to local ATM----
            1. Withdraw Money
            2. Check balance
            3. Add balance
            4. exit
            ''')

            choice = input('Enter your choice:')

            if choice=='1':
                self.withdraw()
            elif choice=='2':
                self.checkbalance()
            elif choice=='3':
                self.addbalance()
            elif choice=='4':
                print('Thanking for using our software')
                break
            else:
                print('Invalid Input')

            
    def withdraw(self):
        temp = int(input('Enter the amount you want to withdraw:'))
        if self.balance > temp:
            print('Withdrew amount successfully')
            self.balance-=temp
        else:
            print('Insufficient balance')


    def checkbalance(self):
        print('Your current balance is',self.balance)
    
    def addbalance(self):
        temp = int(input('Enter the amount you want to add:'))
        self.balance += temp


Niroj = Atm()

