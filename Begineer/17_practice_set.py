# qn 1
marks = []

physics = int(input("Enter physics marks:"))
marks.append(physics)
chemistry = int(input("Enter chemistry marks:"))
marks.append(chemistry)
maths = int(input("Enter maths marks:"))
marks.append(maths)
biology = int(input("Enter biology marks:"))
marks.append(biology)
computer = int(input("Enter computer marks:"))
marks.append(computer)

print(marks)

#qn 2
sum = 0
for mark in marks:
    sum += mark

percentage = sum/5

print("Total marks =",sum)
print("Total percentage =",percentage)


#qn 3
no_of_ones = 0
A = (1, 2, 1, 9, 1, 4, 3, 1, 1, 11)

for item in A:
    if item==1:
        no_of_ones+=1

print(no_of_ones)
