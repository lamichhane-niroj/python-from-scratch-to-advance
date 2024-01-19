#qn 1
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))
f = int(input("Enter a number: "))
g = int(input("Enter a number: "))
h = int(input("Enter a number: "))

set = {a,b,c,d,e,f,g,h}
print(set)

#qn 2
s = {1, "1", 1.0}
print(s)

#qn 3
mydict = {}
mydict["Nepal"] = "Kathmandu"
mydict["Bangladesh"] = "Dhaka"
mydict["Bhutan"] = "Thimphu"
mydict["Us"] = "Washington"
print(mydict)

#qn 4 i) It overwrites the previous key:value
mydict["Nepal"] = "N"  
print(mydict)

#qn 4 ii) It just add an another keypair
mydict["kathmandu"] = "Kathmandu" 
print(mydict)

#qn 5
#No list cannot stored in a set as list is hasable but set is unhasable
set = {1,2,3,[4,5,6]}  #generates error
