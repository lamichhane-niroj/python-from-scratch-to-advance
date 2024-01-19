#qn 1
for i in range(10):
    print("12 x " + str(i+1) + " =", 12*(i+1))


#qn 2
num = int(input("Enter a number: "))
is_prime = True

for i in range(2, (num-1), 1):
    if(num%i == 0):
        is_prime = False
        break

if(is_prime):
    print("Prime")
else:
    print("Not prime")


# qn 3
def value(n):
    summ = 0
    factorial = 1
    for i in range(1,n+1):
        summ+=i
        factorial*=i
    return summ,factorial


num = int(input("Enter a number: "))
s,f = value(num)
print(s,f)



#qn 4
str = "programming"
length = len(str)

for i in range(int(length/2)):
    for j in range(i, length-i):
        print(str[j],end = "")
    print("")


# qn 5
n = 5
for i in range(n):
    for space in range(n-(i+1)):
        print("  ",end="")
    
    for j in range(2*i+1):
        print("* ",end="")
    
    print("")


#qn 6
for i in range(5):
    for j in range(6):
        if i==0 or i==4:
            print("*",end="")
        elif j==0 or j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print("")



