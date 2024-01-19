# json - JavaScript object notation, it is used for data transfer from server to client(browser)

import json

# creating json
my_str = {"name": "Niroj", "lang": "python"}

# converting dictionary to json
my_json = json.dumps(my_str)
print(type(my_json))
print(my_json)

# converting string to json
data = '{"name": "Rohan", "lang": "C++"}'

# print(data['name']) # This gives error

jsonLoad = json.loads(data)

print(jsonLoad['name'])

