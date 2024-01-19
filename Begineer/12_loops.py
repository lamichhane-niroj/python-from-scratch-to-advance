#There are two types of loops in python i.e while and for loop

#while loop -> use when the no of iteration is not fixed but at some point the loop must stop
'''
while(condition):
    statements
'''

i = 0
while(i<10):
    print(i)
    i+=1

fruits = ["apple", "mango", "banana", "papaya", "watermelon"]    
#This is called list similar to array, we will study about it later
j = 0
while j<len(fruits):
    print(fruits[j])
    j+=1


#for loop -> use when the no of iteration is fixed
'''
for i in range(starting_index, stop_index, step_index):
    statements
'''

for k in range(10):
    print(k)

for l in range(0,10,2):
    print(l)

for fruit in fruits:
    print(fruit)
