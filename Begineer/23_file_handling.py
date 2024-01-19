# opening, reading and closing a file
f = open('sample.txt','r')

# read whole data
data = f.read()
print(data)

# read single line
line = f.readline()
print(line)

# reads some character
part = f.read(3)
print(part)

f.close()

# writing a file
f = open('sample.txt','w')
# write by erasing all previous data
f.write("Sasha = 65")
f.close()

# appending a file
f = open('sample.txt','a')
f.write("Hanji = 35\n")
f.close()

# with statement
with open('sample.txt','a') as f:
    f.write("zeek = 60")

