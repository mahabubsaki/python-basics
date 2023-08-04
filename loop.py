''' 
range function creates a sequance of numbers starting from 0 which is default, increaments by 1 which is also default and takes a valid integar parameter where will be the stopage of range, if we print the range stopage will be exluded
'''

'''
if i write range(10) it become range(0,10,1)
we can also set customize value in start and increament
like range range(10,100,10)
'''

'''
loops can be through to list,tuple,string or range

'''

'''
list() function takes a iterable in parameter such as another list,string,tuple or range and create a new list
'''

for each in ["apple", "komola", "lichu"]:
    print(each)

for each in range(10):
    print(each)

for each in "Mahabub Saki":
    if each != " ":
        print(each)


print(list(range(200, 100, -2)))


count = 0

while count < 100:
    if count == 50:
        count += 1
        break
    print(count)
    count += 1  # ++ not exists in python
