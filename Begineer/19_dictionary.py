# dictionary is collection of key:pair value
# unordered, non-duplicate key, modifiable

key_pair = dict(name='Niroj', age=21, city='Itahari')
print(key_pair)

emptydict = {}
print(type(emptydict))

mydict = {
    "Teacher": "one who teaches",
    "Pilot": "one who flies plane",
    "marks": [15, 30, 22],
    "Teacher": "one who beats",  # this only modifies the first key
    "Master": "one who teaches"
}
print(mydict)
# i.e. the dictionary can have same pair but not same key

# modifiable
mydict["Teacher"] = "one who motivates"
print(mydict)
print(mydict["Master"])

mydict = {
    'Student': ['Anish', 'Manoj', 'Roshan', 'Buddha', 'Safal', 'Janak'],
    'Marks': [89.5, 90.2, 88, 86, 85, 87.9],
    'age': [21, 22, 22, 21, 20, 22],
    'ismale': [True, True, True, True, True],
}

mydict['Student'][2] = 'Roshan.k'

print(mydict['Student'][2])
