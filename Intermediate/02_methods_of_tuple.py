#methods of tuple

#creating tuple
my_tup = tuple([1,2,3,4,5])
print(my_tup)

#brackets are optional
my_tup1 = 2,4,6,8
print(my_tup1)

#creating tuple with 1 element
se_tup = (1,)           #looks weird but it is
print(type(se_tup))

#unpacking of tuple
details = 'Niroj','Nepal',21
print(type(details))
name, nation, age = details
print(name,nation,age)

#unpacking using *
tup = 1.1,1.1,3.3,4.4,5.5,6.6,7.7
a, *b, c = tup
print(type(a), a)
print(type(b), b)
print(type(c), c)

#conversion between list and tuple
# tuple to list
my_tuple = (1,2,3,4,5)
my_lst = list(my_tuple)
print(my_lst)

# list to tuple
my_tuple1 = tuple(my_lst)
print(my_tuple1)

#maximum method of list can be used in tuple too like count, index, len
print(tup.count(1.1))
print(tup.index(3.3))
print(len(tup))
print(sum(tup))

