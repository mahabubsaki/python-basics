def myName(fname, lName):
    print(f"Hello {fname} {lName}, How are you?")


myName("Mahabub", "Saki")


# We dont have to maintain the sequance of parameter and argument here instead we can specifiy the parameter in argument

def mysum(one, two):
    print(one/two)
mysum(two=5, one=10)
# lambda function is almost same as js function expression which means we can store it on a varibale

myNameLambda = lambda fname,lName :  print(f"Hello {fname} {lName}, How are you?")

#shortuc version of first function
