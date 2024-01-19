# zip(*iterable) = It aggregate element from two or more iterables, creates the zip object of tuple of pair elements

user = ('abc','cde','efg')
password = (123,345,567)

data = zip(user,password)

print(type(data))

# data1 = list(data)
# print(data1)

# data2 = tuple(data)
# print(data2)

data3 = dict(data)
print(data3)