# set is the collection of unordered, unmodified and non-repetitive Element
b = {}  # empty dictionary
print(type(b))

set = set()  # empty set
print(type(set))

a = {1, 2, 3, 5, 4, 5}
print(a)  # print only non-repetitive element
# a[0] = 5 -> this will throw error

set.add(5)
set.add((5, 6, 7))     # tuple can be added to set as it is unmodifiable
# set.add([1,2,3])   #list cannot be added to set as it is modifiable
# set.add({'apple' = 250, 'banana' = 150 })   #dictionary cannot be added to set as it is modifiable

print(set)

# frozen set - It is the type of set in which no item can be added nor removed
f_set = frozenset([1, 2, 3, 4])
print(f_set)
