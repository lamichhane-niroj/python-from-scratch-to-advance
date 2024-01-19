#qn 1
def sum(n):
    final = 0
    for i in range(n+1):
        final += i
    return final

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("sum = " + str(sum(n)) +" \nfactorial = ",factorial(n))


#qn 2
def mul(n):
    for i in range(10):
        print(str(n) + " x " + str(i+1) + " = ", n*(i+1))

n = int(input("Enter a number: "))
mul(n)



#qn 3
def sum(n):
    if n==1:
        return 1
    return (n + sum(n-1))

def factorial(n):
    if n==1 or n==0:
        return 1
    return (n * factorial(n-1))

n = int(input("Enter a number: "))
print("sum = " + str(sum(n)) +" \nfactorial = ",factorial(n))
