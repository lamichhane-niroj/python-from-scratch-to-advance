
#qn 1
loft = [(11,22),(2,7),(0,0),(200,300),(100,250),(300,150)]
sort_wrt_x = sorted(loft,key=lambda x:x[0])
sort_wrt_y = sorted(loft,key=lambda x:x[1])
print(sort_wrt_x)
print(sort_wrt_y)


#qn 2
lofd = [{2:1},{4:0},{3:2},{1:6},{5:5}]
sort_wrt_key = sorted(lofd,key=lambda x:list(x.keys()))
sort_wrt_value = sorted(lofd,key=lambda x:list(x.values()))
print(sort_wrt_key)
print(sort_wrt_value)


#qn 3
natural = [1,2,3,4,5,6,7,8,9,10]
func = list(filter(lambda x: x%2==0 ,natural))
print('Even:',len(func))
print('Odd:',len(natural)-len(func))


#qn 4
square = list(map(lambda x:x**2,natural))
cube  = list(map(lambda x:x**3,natural))
print(f'Square {square} \nCube {cube}')


#qn 5
word = 'python'
check = lambda x: True if x.startswith('p') else False
print(check(word))


#qn 6
lst = [1,-1,2,-2,5,-5,3,-6,4,-4]
result = sorted(lst,key=lambda x: 0 if x==0 else -1/x)
print(result)

