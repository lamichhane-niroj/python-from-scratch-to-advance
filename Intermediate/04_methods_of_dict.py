#method of dictionary

my_dit = dict(name = 'Niroj', city = 'Itahari', email = 'abcxyz123')

#copy method - same goes to dict as list
my_dict = my_dit.copy()
my_dict['age'] = 21     #adds key pair to the dict
print(my_dict)

#del function - It deletes the given key pair from the dictionary
del(my_dict['age'])
print(my_dict)

#pop method -  It deletes the given key pair from the dictionary
my_dict.pop('email')
print(my_dict)

#pop item method - It deletes the last key pair from the dictionary
my_dict.popitem()
print(my_dict)

#keys method - It returns all the keys of dictionary
print(my_dit.keys())

#values method - It returns all the values of dictionary
print(my_dit.values())

#item method - It returns all the keys and values of dictionary
print(my_dit.items())

#using for loop
for keys in my_dit.keys():
    print(keys)

for values in my_dit.values():
    print(values)

for keys,values in my_dit.items():
    print(keys, values)

#update method - It merges two dictionary
marks = {'maths':90,'science':92,'python':98,'Name':'Niroj'}
details = dict(maths_score='A',science_score='A+',python_score='A+',Name ='Jorin')
marks.update(details)
print(marks)

#get method - It returns the value if present else return None
print(marks.get("Name"))

#default method
marks.setdefault('Practical')
print(marks)

#clear method - It clears the dictionary
marks.clear()
print(marks)


