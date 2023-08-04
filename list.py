friends = ['a', 'b', 's', 'c']

print(friends[-4])

# list index start from negetive version of size of list to postive version of size-1
# in above case range is from -4 to 3 where -1 and 0 both are same index


my_list = list(range(0, 101))

sliced_list = my_list[10:92:2]

# we can slice from a list and create a new list by : in [] the visualization will be list_we_want_to_slic[start:stop:step(optional)]

# print(sliced_list)

# list methods


# merge we can merge 2 or more list b + operator

list_one = [1, 2, 3]
list_two = [4, 5, 6]


merge_list = list_one + list_two


# append() same as array push() method in js which add element in list
# copy() same as create new array with spread oprator in js
# insert() same as array splice() method which adds a element in specific index
# count() counts a specific elements count in a list

numbers = [2, 2, 2, 2, 1, 2]


two_count = numbers.count(2)  # this will return 5
# pop() same as js pop() method returns the popped element if we place it on a variable
# remove() remove first element given in parameter
# clear() empty the list
# reverse() same as array reverse() method
# sort(reverse=True) descending order of list and sort(reverse=False) asceding order of lis. this method actually mutatue the original list. dont return anything
#
