"""
1. Iterable-Those object which can be iterated over to access its element. eg- list,tuple,dict,set,range, -effect
2. Iteration- It is the process of iterating over the iterable object, -process
3. Iterator- It is the object which iterate over the iterable object, -cause
"""
   
# Iterator must have two dunder method __next__,__iter__
# lets check
lst = [1, 2, 3, 4, 5]
tup = 1, 2, 3, 4, 5
my_dict = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
my_set = {1, 2, 3, 4, 5}
ranged = range(5)

print(type(lst), type(tup), type(my_dict), type(my_set))

# checking if iterable object are itself iterator - NO

# print(dir(lst)) 
# print(dir(tup))
# print(dir(my_dict))
# print(dir(my_set))
# print(dir(ranged))

# since these all iterable object only has iter method. So, they are not iterators

# To create iterator we use the iter method
lst_iter = lst.__iter__()
tup_iter = tup.__iter__()
my_dict_iter = my_dict.__iter__()
my_set_iter = my_set.__iter__()
ranged_iter = ranged.__iter__()

# checking iterators have __next__() method - YES

# print(dir(lst_iter)) 
# print(dir(tup_iter))
# print(dir(my_dict_iter))
# print(dir(my_set_iter))
# print(dir(ranged_iter))

# To access the element using iterators we use next method
while True:
    try:
        print(lst_iter.__next__())
        print(tup_iter.__next__())
        print(my_dict_iter.__next__())
        print(my_set_iter.__next__())
        print(ranged_iter.__next__())
        
    except StopIteration:
        break


# conclusion - Every iterator is an iterable object but every iterable object is not iterators


# making my own for loop using iterators
num = [2,4,6,8]
# for i in num:
#     print(i)   # How is this printing, i haven't done an increment 

# step-1 python creates an iterator of that object
iter_num = iter(num)
# step-2 python uses the next dunder method of the iterator
try:
    print(next(iter_num))
except:
    StopIteration()


# creating my own for loop
def myownforloop(iterable):
    iterator = iter(iterable)
    
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


lst = [1, 2, 3, 4, 5]
myownforloop(lst)


# Why to use range function over the technique of storing data to list?
import sys

values = [x for x in range(10000)] # This stores all the data in the memory

value = [range(10000)] # This stores only one data at a time by creating iterator

# memory used by them has a vast difference
print(sys.getsizeof(values),"bytes")
print(sys.getsizeof(value),"bytes")
