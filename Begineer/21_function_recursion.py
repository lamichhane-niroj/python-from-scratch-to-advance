# function
def average(marks):
    p = (marks[0]+marks[1]+marks[2]+marks[3])/4
    return p
    
marks = [30, 60, 89, 50]
print(average(marks))

# default argument function
def greet(name="Stranger"):
    print("Good Day " + name)


greet("Niroj")
greet()


# recursion
def factorial_recursive(n):
    if(n==1 or n==0):
        return 1
    return n * factorial_recursive(n-1)


print(factorial_recursive(6))


# function returning multiple values
def func(n):
    # getting prime
    val = True
    for i in range(2,n//2,1):
        if n%i==0:
            val = False

    # sum to n natural number
    summ = 0
    for i in range(n+1):
        summ+=i
    
    # factorial of a number
    fact = 1
    for i in range(1,n+1):
        fact*=i
    
    return val,summ,fact


v,s,f = func(12)

if(v):
    print('prime',', sum = ',s,', factorial = ',f)
else:
    print('Not prime',', sum = ',s,', factorial = ',f)


