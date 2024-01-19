# itertools - product, permutations, combinations, accumulate, groupby, and infinite iterators

# product - It returns the iterator of cartesian product
from itertools import product
a = [1,2]
b = [3,4]
c = [5]
pro = product(a, b)
pro2 = product(a, c, repeat=2)
print("##### Product #####")
print(list(pro))
print(list(pro2))


# permutation - It returns all the possible ordering of input
from itertools import permutations
a = [1, 2, 3]
per = permutations(a)
per2 = permutations(a, 2)
print("##### Permutations #####")
print(list(per))
print(list(per2))

# combination - It returns all possible grouping of input of given length
from itertools import combinations
# for replacement using function combination_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print("##### Combinations #####")
print(list(comb))


# accumulate - It returns the index with sum of every index before it which is default
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print("##### Accumulate #####")
print(a)
print(list(acc))

# for other operation
import operator
acc2 = accumulate(a,func=operator.mul)
print(list(acc2))


# groupby - It groups the element according to given condition
from itertools import groupby
# grouping on given condition

a = [1, 2, 3, 4]
group_obj = groupby(a, lambda x: x > 2)

print("##### GroupBy #####")
for key,value in group_obj:
    print(key, list(value))


# grouping according to age
lst = [dict(name = 'Niroj', age= 21), dict(name = 'manoj', age = 21), dict(name = 'roshan', age = 22),
    dict(name = 'safal', age = 20)]

group_age = groupby(lst, lambda x:x['age'])

for key,value in group_age:
    print(key, list(value))


# infinite iterators - count, cycle, repeat
from itertools import count,cycle,repeat
# count - started counting infinitely from 10 with given step
for i in count(10,2):
    print(i,end=" ")
    if i==100:
        break

# cycle - repeated cycle infinitely
a = [1, 2,  3]
count = 0
for i in cycle(a):
    print(a, end=" ")
    if count==100:
        break
    count += 1

# repeat - repeat the same thing infinitely and stopping index can be given
for i in repeat(1,4):
    print(i)
