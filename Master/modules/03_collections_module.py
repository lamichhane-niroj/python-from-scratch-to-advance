# collections - Counter, namedtuple, OrderedDict, DefaultDict, deque

# Counter
from collections import Counter
# counter returns the dictionary with key of element and values of occurrence
a = 'aaaaabbbbcccdde'
b = [1, 2, 3, 1, 2, 3, 1, 2, 3]
c = (1, 2, 3, 3, 2, 1, 1, 1, 1)

my_str_counter = Counter(a)
my_lst_counter = Counter(b)
my_tuple_counter = Counter(c)

print(my_lst_counter)
print(my_str_counter)
print(my_tuple_counter)

# methods of counter - As Counter returns the counter dictionary so every method of dictionary is counter method
print(my_tuple_counter.most_common(1))  # returns the most repeated element
print(my_str_counter.total())           # returns the sum of repeated element
print(list(my_lst_counter.elements()))  # returns the element of dictionary


# namedtuple
from collections import namedtuple
# namedtuple creates a class and the element of given name
point = namedtuple('point','x,y')
pt = point(10,5)
print(pt)
print(pt.x, pt.y)


# OrderedDict
from collections import OrderedDict
# OrderedDict maintains the order in which object is inserted
my_dict = OrderedDict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
my_dict['d'] = 4
print(my_dict)


# defaultdict
from collections import defaultdict
# defaultdict has default values for a key
my_dit = defaultdict(float) # any datatype can be given like int,float,str,bool,complex,list,tuple,dict,set
print(my_dit['a'])


# deque
from collections import deque
# deque can be treated like list with extra functionality
d = deque()

for i in range(5):
    d.append(i)

d.appendleft(5) # appending from left side element
d.popleft()     # poping from left side element
d.extendleft([9,8,7])   # extending list from left side
d.rotate(2)             # pushes element towards right for given no of times, for left side given - number

print(d)





