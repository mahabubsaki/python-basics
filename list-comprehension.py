# in js we use map and filter to do calculation and create new array from an array. here we can also do this but with a single line
# sytanx [calculation for item(any name) in list(from which list or iterable we want to create) if condition(for filtering we have to give conditions here but it is optional)]

# we can do multiple condition like if i > 4 or i < 8

list_1 = [2, 4, 5, 6, 7, 8, 3]
list_2 = [i*10 for i in list_1 if i > 4 and i < 8]

print(list_2)

# we can do if else condition while list comprehension

my_list = range(1, 21)

odd_even_list = ["even" if i % 2 == 0 else "odd" for i in my_list]

print(odd_even_list)


two_dimension = [[2, 4, 2], [3, 6, 3]]

# conversion = []

# for i in range(3):
#     c = []
#     for j in two_dimension:
#         c.append(j[i])
#     conversion.append(c)

# shortcut method
conversion = [[col[row] for col in two_dimension] for row in range(2)]

print(conversion)
