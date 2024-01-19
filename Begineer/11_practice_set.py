#qn 1
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b:
    if a>c:
        print(a, "is the greatest")
    else:
        print(c, "is the greatest")
else:
    if b>c:
        print(b, "is the greatest")   
    else:
        print(c, "is the greatest")


#qn 2
physics = int(input("Enter physics marks:"))
chemistry = int(input("Enter chemistry marks:"))
maths = int(input("Enter maths marks:"))
biology = int(input("Enter biology marks:"))
computer = int(input("Enter computer marks:"))

percentage = (physics+chemistry+maths+biology+computer)/5

if percentage > 80:
    print("Distinction with percentage",percentage,"%")
elif percentage > 70:
    print("First division with percentage",percentage,"%")
elif percentage > 60:
    print("second division with percentage",percentage,"%")
elif percentage > 40:
    print("Third division with percentage",percentage, "%")
else:
    print("fail with percentage",percentage, "%")


#qn 3
year = int(input("Enter the year:"))

is_leap_year = False

if year%4 != 0:
    is_leap_year = False
else:
    if year%100 != 0:
        is_leap_year = True
    else:
        if year%400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
   
if is_leap_year:
    print("Leap year")
else:
    print("Not a leap year")


#qn 4
can_vote = False

print("\t\t\tPlease fill the form below")
age = int(input("Age: "))
country = input("Nationalism: ")
citizen = (input("Do you have citizenship card(yes or no): "))
voter = (input("Do you have voter card(yes or no): "))

if(age >= 18 and (country == "Nepal" or country == "nepal") and citizen == "yes" and voter == "yes"):
    print("You are ready to vote")
else:
    print("sorry!, You cannot vote")
 

#qn 5
string = input("Enter a string: ")
rev_string = string[::-1]

if string == rev_string:
    print("String is pallindrome")
else:
    print("String is not pallindrome")