
# list comprehension
lst = [1,2,3,4,5]
sq_lst = []

# normal method
for i in lst:
    sq_lst.append(i*i)

print(lst)
print(sq_lst)

# list comprehensive
com_lst = [i*i for i in lst]

print(lst)
print(com_lst)

# we can also place conditional like if else
marks = [20,36,72,34,11,17,32,99,60]
flt_marks = list(filter(lambda x:x >= 32,marks))

print(marks)
print(flt_marks)
 
flter_marks = [i for i in marks if i>=32]
flter_marks_with_else = [i if i>=32 else 'Failed' for i in marks]

print(flter_marks)
print(flter_marks_with_else)


# dict comprehension
marks = {'Rohan':32,'Anish':55,'Manoj':67,'Niroj':76,'Prasit':67,'Babu':16,'Sona':31}

percent = {keys: (values/80*100) for keys,values in marks.items()}

print(percent)

# with if statement
with_if_statement = {keys:values for keys,values in percent.items() if values >= 70}
print(with_if_statement)

# with if else statement
with_if_else_statement = {keys:(values if values >= 70 else 'Less') for keys,values in percent.items()}
print(with_if_else_statement)

# with function
def check(value):
    if value>=32:
        return value
    else:
        return 'Fail'
        
with_func = {keys:check(value) for keys,value in marks.items()}
print(with_func)
