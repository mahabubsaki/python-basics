# lower() same as toLowerCase() in js
# upper() same as toUpperCase() in js
# isLower() return true if string is lowercase
# isUpper() return true if string is uppercase
# title() convert the string to title case like from hello world to Hello World
# isTitle() return true if string is titlecase
# capitalize() makes the strings first letter uppercase and all other lowercase
# swapcase() converts lowercase to uppercase and uppercase to lowercase
# casefold() same as lower() but more eficient
# replace() creates a new string from actual string. syntex replace(element,new value,count(it is optional which means if not given all target element will be replaced but if given then replace operation will be done to count))
# count() counts the corresponding letter in string in given parameter
# isDigit() return true if string have only numbers

# join() same as js but join is a string method which takes a list

# split() same as js but split is also a string method which takes a list


myFriends = ["a", "b", "c"]

new_string = "-".join(myFriends)

my = new_string.split("-")
print(my)

a = "hello world"

b = a.title()

c = b.istitle()


d = "Mahabub Saki"


e = d.replace(d[-1], "I", 1)
print(e)


# we can also create template string like js we have to give f keyword in front of string to make it like template string

name = "Saki"

age = 20

sentence = f"My name is {name} and I am {age} years old"

print(sentence)
