def myName(fname, lName):
    print(f"Hello {fname} {lName}, How are you?")


myName("Mahabub", "Saki")


# We dont have to maintain the sequance of parameter and argument here instead we can specifiy the parameter in argument

def mysum(one, two):
    print(one/two)
mysum(two=5, one=10)
# lambda function is almost same as js function expression which means we can store it on a varibale

myNameLambda = lambda fname,lName :  print(f"Hello {fname} {lName}, How are you?")


myNameLambda("Jack","Wick")

#shortuc version of first function




# rest parameter in js we use ... and here we use *

def all_sum(*arg):
    sum = 0
    for i in arg:
        sum+=i
    return sum

print(all_sum(2,2,3))

# we can also use non sequantial parameter in python

def full_name(fname,lname):
    return f"{fname} {lname}"

print(full_name(lname="Saki",fname="Mahabub"))

# if functions parameter number is unknown and we are passing arguments as key value pair (lname="saki") then we can convert it into dictionary (in js we call it object)

def params(**allParams):
    arr = []
    for key,value in allParams.items():
        arr.append([key,value])
    return arr
print(params(name="Mahabub Saki",currentClass="BSC"))
