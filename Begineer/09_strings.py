#unmodified, ordered, duplicate

#concatination of string
First_Name = "Niroj"
Last_Name = "Lamichhane"
Full_Name = First_Name +" "+ Last_Name  #concatenation of string

print("My name is:",Full_Name)

'''
    indexing 
    hello bro
    012345678
  -(987654321)
'''

#slicing of string [starting_index: stopping_index: step]
print(Full_Name[2:7])    #gives string from 2 to 6
print(Full_Name[0:])     #gives string from 0 to end
print(Full_Name[:10])    #gives string from start to 9
print(Full_Name[3:15:3]) #gives string from 3 to 14 with step 3
print(Full_Name[-5:-1]) 

print(Full_Name[:])     
print(Full_Name[::])   
print(Full_Name[1::3]) 
print(Full_Name[2:])


