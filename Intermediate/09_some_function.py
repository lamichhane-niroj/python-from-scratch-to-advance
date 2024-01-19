#lamda is a one line function which takes argument and returns expression
#lamda argument: expression

#add func
add10 = lambda x: x+10

#is similar to
def add10_func(x):
    return x+10

print(add10(15))

#lamda function with multiple argument
mult = lambda x,y: (x+y)
print(mult(10,2))

#sorted function 
points = [(1,2,4),(0,0.4,3),(1.5,3,5),(-1,-2,1)]
#default wrt x
sortedpointsx = sorted(points)

#sorted according to y
sortedpointsy = sorted(points,key= lambda x: x[2])
print(sorted(sortedpointsy))

#sorted according to x+y
sortedpointxy = sorted(points,key = lambda x:x[0]+x[1]+x[2])
print(sortedpointxy)

#map function
#This function maps the element according to the condition
#map(func,seq)

a = [1,2,3,4,5]
#we want to multiply each element with 3, we can use technique or map func

# map func
mul_by_3 = map(lambda x:x*3,a)
print(list(mul_by_3))

#also using technique
mul = [x*3 for x in a]
print(mul)

#filter function
#This function filter element according to the condition
# filter(func,seq)

b = [1,2,3,4,5,6]
#now i need only odd, we can use technique or filter func

#filter func
odd_num = filter(lambda x:x%2==1,b)
print(list(odd_num))

#also using technique
odd = [x for x in b if x%2==1]
print(odd)

#reduce function
#This function reduces element according to the condition
# reduce(func,seq)

from functools import reduce

c = [1,2,3,4,5,6]
#now to calculate the value of each item such that it is the product precedding element
fact = reduce(lambda x,y: x*y, c)
print(fact)