#method of list

#scalar list - Gives a list of same elements of no of times
s_lst = [0]*5 
print(s_lst)

#append method - It adds another element at the end of the list
lst = [1.9,0.5,1.2,7.2,5]
lst.append(6)
print(lst)

#sort method - It sorts the element of original data in increasing order or alphabetical order
lst.sort()
print(lst)
animals = ['cat','dog','camel','ant','bear']
animals.sort()
print(animals)

#pop method - It pop the last element of list and returns the last element
element = lst.pop()
print(lst, element)

#clear method - It clears the list
lst.clear()
print(lst)

#insert method - It inserts the element in the given index
animals.insert(4,'cow')
print(animals)

#reverse method - It reverse the element of the original data
animals.reverse()
print(animals)

#extend method - It joins two list, we can also do this by using + operators
cars = ['bmw','Tesla','ferrari']
fruits = ['apple', 'banana', 'cherry']
fruits.extend(cars)  
print(fruits)

#remove method - It removes the given element from the list
animals.remove('bear')
print(animals)

#len function - It gives the length of the list
print(len(animals))

#count method - It counts the occurance of the element
print(animals.count('deer'))

#index method - It gives the index of the element
print(animals.index('cat'))

#sum function - It sums the list
num_lst = [2,4,6,8,1,3,5,7,9]
print(sum(num_lst))

#copy a list
lst1 = ['Apple','Cherry','Banana']

lst2 = lst1
#This above copying can create a problem i.e the changes in copy will reflect in original data because the location for both list is same
print(lst1, lst2)
lst2.append('Mango')  
print(lst1, lst2)

#method 1- for copying - using for keyword
lst3 = [i for i in lst1]
lst3.append('watermelon')
print(lst1, lst3)

#method 2- for copying - using copy method
lst4 = lst1.copy()
lst4.append('Grape')
print(lst1,lst4)

#method 3- for copying - using slicing concept
lst5 = lst1[::]
lst5.append('Avocado')
print(lst1, lst5)

#method 4 - for copying - using list keyword
lst6 = list(lst1)
lst6.append('Jackfruit')
print(lst1, lst6)



