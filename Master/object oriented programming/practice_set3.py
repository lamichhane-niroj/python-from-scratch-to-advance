class Binary:
    #binary to decimal
    def bin2dec(self, num):
        self.bn = str(num)
        l = len(self.bn)
        result = 0
        self.bn = int(self.bn)
        for i in range(l):
            var = self.bn%10
            self.bn = int(self.bn/10)
            result += var * pow(2,i)
        return result
        
    #binary to octal
    def bin2oct(self, num):
        self.bn = str(num)
        l = len(self.bn)
        result = 0
        self.bn = int(self.bn)
        for i in range(l):
            var = self.bn%10
            self.bn = int(self.bn/10)
            result += var * pow(8,i)
        return result

class Decimal:
    #decimal to binary
    def dec2bin(self, num):
        self.dn = num
        result = []
        while self.dn != 0:
            var = self.dn % 2
            self.dn = int(self.dn/2)
            result.append(var)
        return result
    
    #decimal to octal
    def dec2oct(self, num):
        self.dn = num
        result = []
        while self.dn != 0:
            var = self.dn % 8
            self.dn = int(self.dn/8)
            result.append(var)
        print(result)

class Octal:
    #octal to decimal
    def oct2dec(self, num):
        self.on = str(num)
        l = len(self.on)
        result = 0
        self.on = int(self.on)
        for i in range(l):
            var = self.on%10
            self.on = int(self.on/10)
            result += var * pow(8,i)
        return result

    #octal to binary
    def oct2bin(self, num):
        self.val = self.oct2dec(num)
        result = []
        while self.val != 0:
            var = self.val % 2
            self.val = int(self.val/2)
            result.append(var)
        return result[::-1]

binary = Binary()
decimal = Decimal()
octal = Octal()
while True:
    print('''Choose an option: 
           1. Binary to Decimal
           2. Binary to Octal
           3. Decimal to Binary
           4. Decimal to Octal
           5. Octal to Binary
           6. Octal to Decimal
           7. Exit
    ''')
    choice = int(input("Enter choice: "))
    if choice == 1:
        num = int(input("Enter a binary number: "))
        print(binary.bin2dec(num))
    elif choice == 2:
        num = int(input("Enter a binary number: "))
        print(binary.bin2oct(num))
    elif choice == 3:
        num = int(input("Enter a decimal number: "))
        print(decimal.dec2bin(num))
    elif choice == 4:
        num = int(input("Enter a decimal number: "))
        print(decimal.dec2oct(num))
    elif choice == 5:
        num = int(input("Enter a octal number: "))
        print(octal.oct2bin(num))
    elif choice == 6:
        num = int(input("Enter a octal number: "))
        print(octal.oct2dec(num))
    else:
        break
    






    
