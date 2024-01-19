#method of set

#creating of set
my_set = {1,2,3,2,5,1,7}
print(my_set)

#using set class
my_set = set('hello')
print(my_set)

#empty set
my_set = set()

#add method- It adds the element to the set
my_set.add(5)
for i in range(10):
    my_set.add(i)

print(my_set)

#copy method - It is similar to list
new_set = my_set.copy()
print(new_set)

#remove method- It removes the given element from the set and if no element is found it throw error
my_set.remove(3)
print(my_set)

#discard method- It removes the given element from the set and if no element is found it doesnot throw error
my_set.discard(4)
print(my_set)

#pop method - It pop the first element
my_set.pop()
print(my_set)

#clear method - It clears the set
my_set.clear()
print(my_set)

#operations with set
odd_num = {1,3,5,7,9}
even_num = {2,4,6,8}
prime_num = {1,3,5,7}

#union method - returns union of two sets
u = odd_num.union(even_num)
print(u)

#intersection method - returns intersection of two sets
i = odd_num.intersection(prime_num)
print(i)

#difference method - returns difference of two sets
A = {1,2,3,4,5}
B = {3,4,5,6,7}

dif = A.difference(B)
print(dif)

#symmetric difference method - returns symmetric difference of two sets = (A-B)u(B-A)
sys_dif = A.symmetric_difference(B)
print(sys_dif)

#update method - merges two set and returns to first one
A.update(B)
print(A)

#intersectionupdate method - update the intersecting element to the first set
C = {1,2,3,4,5}
C.intersection_update(B)
print(C)

#differenceupdate method - update the difference to first set
A.difference_update(B)
print(A)

#symmetric_difference_update method - update the symmetric difference to first set
A.symmetric_difference_update(B)
print(A)

#subset and superset method- return True if it is else false
Sub = {1,2,3}
Super = {1,2,3,4,5}
print(Sub.issubset(Super))
print(Super.issuperset(Sub))

#isdisjoint - return True or false
print(Sub.isdisjoint(Super))
