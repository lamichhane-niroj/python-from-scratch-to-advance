#Arthimetic operators +,-,/,*,%,**,//
print("The result of 10+5 is ",10+5)
print("The result of 10-5 is ",10-5)
print("The result of 10*5 is ",10*5)
print("The result of 10/5 is ",10/5)
print("The result of 10%5 is ",10%5)
print("The result of 10//5 is ",10//5)
print("The result of 10**2 is ",10**2)

#Assignment operators =, +=, -=, *=, /=  
#multiple assignment 
English = Maths = Mechanics = Drawing = 32
# this is the unpacking of tuple
Name, SymbolNo, University, Grade = "Ram", 1005, "Tribhuwan", 3.2

a = 10
a+= 1  #equivalent to a = a+1
print("The result is",a)

# + sign is also used for concatenation of string
print("Niroj"+ " "+"lamichhane")

a-=1  #equivalent to a = a-1
print("The result is",a)

a*=5  #equivalent to a = a*5
print("The result is",a)

a/=2  #equivalent to a = a/2
print("The result is",a)

# comparision operators ==, <=, >=, >, <, !=
b = (14 >= 6)   #Is 14 greater than or equals to 6?
print(b)

a = (14 <= 6)  #Is 14 lesser than or equals to 6?
print(a)

c = (a == b)  #Is 14 equals than to 6?
print(c) 

d = (a != b)  #Is 14 not equals to 6?
print(d)

# logical operators - and or not
bool1 = True
bool2 = False
bool3 = (bool1 or bool2)  #returns true if both or one is true
print(bool3)

bool3 = (bool1 and bool2)  #returns true if both are true
print(bool3)

bool3 = (not bool2)  #returns true if false and return false if true
print(bool3)

