#qn 1
lst = [1,2,3,4,5,6,7]
new_lst = [i*i for i in lst]
print(new_lst)

#qn 2
total = sum(new_lst)
print(total)

#qn 3
tup = (1,)
print(type(tup))

#qn 4
import sys
lst = ['Hello',1.1,10000,True,1+2j]
tup = ('Hello',1.1,10000,True,1+2j)

print(sys.getsizeof(lst), "bytes")
print(sys.getsizeof(tup), "bytes")
#Tuple takes less size than list for same data

import timeit
print(timeit.timeit(stmt="['Hello',1.1,10000,True,1+2j]",number=1000000))
print(timeit.timeit(stmt="('Hello',1.1,10000,True,1+2j)",number=1000000))
#It is also clear that tuple takes lesser time to execute the same data for number of times

#qn 5
def add(t,n):
    lst = list(t)
    lst.append(n)
    t = tuple(lst)
    return t

tup = (1,2,3,4,5)
print(tup)
tup = add(tup,6)
print(tup)

#qn 6
tup = 1,2,[3,4,5],6
print(tup)
lst = [1,2,(3,4,5),6]
print(lst)

#qn 7
tup = ('e','l','e','p','h','a','n','t')
if 'e' in tup:
    print('Yes')
else:
    print('no')

#qn 8
name = ('N','I','R',"O",'J')
print(name[::-1])