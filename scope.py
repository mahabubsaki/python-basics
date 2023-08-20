# in js we can change any global variables in any functions but in python we cant do that directly. To do this we have to write a special keyword "global" and the global variable name.

global_var = 2000

def reduce_global_var():
    global global_var
    global_var = global_var - 100 # this will give me error if we dont write previous line
    return global_var


print(reduce_global_var())