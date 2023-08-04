age = input()

# int() function takes string version of a integar and converts it into actual integar in js we call it parseInt()
# float() function takes string version of a float and converts it into actual float in js we call it parseFloat()
# type() function tell the type of variable in js we call it typeof()

age = int(age)

if age >= 18:
    print("adult", type(age))
else:
    print("child")
