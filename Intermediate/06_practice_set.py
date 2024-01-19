#qn 1
my_dict = {'#FF0000':'Red', '#00FFFF':'Cyan','0000FF':'Blue','FFFF00':'Yellow'}

my_dict.update(dict(white = 'FFFFFF'))
print(my_dict)

#qn 2
my_dict = {}
for i in range(10):
    my_dict[i] = i*i

print(my_dict)

#qn 3
mylst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
myset = set()

for i in range(7):
    for values in mylst[i].values():
        myset.add(values)
        
print(myset)


#qn 4
my_dict = {1:1,2:4,6:36,4:16,5:25}
lst = []

for keys in my_dict.keys():
    lst.append(keys)

print(max(lst))

#qn 5
lst1 = [1,2,3,4,5]
lst2 = [1,4,9,16,25]
mydit = {}

for i in range(len(lst1)):
    mydit[lst1[i]] = lst2[i]

print(mydit)

#qn 5
my_dict = {}
for i in range(10):
    my_dict[i] = i*i

#qn 6
def invert(d):
    mydit = {}
    for keys,values in d.items():
        mydit[values] = keys
    return mydit


my_dict = invert(my_dict)
print(my_dict)


