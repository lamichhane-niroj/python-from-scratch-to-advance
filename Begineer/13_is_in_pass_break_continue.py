# in keyword
#it is mostly used in loop, it runs through every pointer

states = ["Texas", "California", "Washington", "Colorado", "Hawaii", "North dacota"]
for state in states:
    print(state)

if "Texas" in states:
    print("Texas exists")

#is keyword
#it is mostly used in conditional statements, it compares variable with its value

var = None
if var is None:
    print("none")

check = False
if check is True:
    print("True")
else:
    print("False")

#break and continue statement
for i in range(0,10,1):
    if i == 4:
        continue  #it skips the statement return below it
    print(i)
    if i == 8:
        break     #it breaks the loop

for i in range(5):
    if i == 2:
        pass      #it does nothing
    print(i) 
