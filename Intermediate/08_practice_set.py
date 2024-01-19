#qn 1
a = float(input('Enter first number:'))
b = float(input('Enter second number:'))

print('The sum of two numbers is %f'%(a+b))
print('The sum of two numbers is {}'.format(a+b))
print(f'The sum of two numbers is {a+b :.2f}')


# qn 2
text = 'Hello everyone i m learning python programming'
my_dict = {}
for items in text.lower():
    my_dict[items] = text.lower().count(items)

print(my_dict)


#qn 3
text = 'shooting scattershot'
first = text[0]
remain = text[1:]
convert = remain.replace(first,'$')

final = first + convert
print(final)


#qn 4
def add(s):
    s = s.lower()
    if len(s) >= 3 and not s.endswith('ing'):
        return s + 'ing'
    elif s.endswith('ing') and len(s)>=3:
        return s + 'ly'
    else:
        return s

text = 'string'

print(add(text))
print(add('fly'))
print(add('aa'))


#qn 5
text = 'Hello world'

def exchange(s):
    start = s[0]
    end = s[-1]
    body = s[1:-1]
    return end + body + start

print(exchange(text))


#qn 6
text = 'bishal,manish,manoj,bibek,anish,biswash,dinesh,happy,milan,niroj,binay,arjun,pawan'
lst = text.split(',')
lst.sort()
print(lst)


#qn 7
text = 'I Am From Nepal'
count = 0

for i in range(4):
    if text[i].isupper():
        count+=1

if count==2:
    newtext = text.upper()
    print(newtext)
else:
    print(text)




