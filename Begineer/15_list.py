#list are the containers that can stores the values of different datatypes
#list are ordered, replaceable, duplicate 
#1-D list
empty_list = []

# creating list
lst = list((1,2,3))
print(lst)

print(empty_list)
continents = ["Asia", "Africa", "South America", "Antartica", "Europe", "North America", "Australia", 5, 7.2, True]

#ordered
for i in range(10):
    print(continents[i])
print("")

#replacable
continents[2] = "Australia"
continents[6] = "South America"

print(continents)

#duplicate
continents[1] = "Asia"
print(continents)
print("")

# searching in list
print("Asia" in continents)

#slicing of list
print(continents[2:])
print(continents[:5])
print(continents[-4:-1])

#2-D list
multidimensional_list = [1,2,3,4,[-5,-6, -7]]
print(multidimensional_list[4][0])
