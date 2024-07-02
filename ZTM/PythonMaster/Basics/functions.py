# Arguments vs Parameters
# Arguments: Values that are sent when the function is called
# Parameters: variables that will be sent to the function 

# Parameters
def say_hello(name):
    print(f"Hello, {name}")

# Arguments
say_hello("Emanuel")

# Docstrings - Documents what it does and needs like built in functions do
def test(a):
    '''
    Info: this function test and prints param a
    '''
    print(a)

test("!!!!!")
help(test) # You can also use this to see the documentation
print(test.__doc__) # You can also use this instead

# *args and **kwargs
# *args - when you don't know how many params will be received (treats it as a tuple)
# **kwargs - same as args but you can name keywords (treats it as a dictionary)

# Rule: params, *args, default params, **kwargs

def super_fun(*args):
    return sum(args)

print(super_fun(1,2,3,4,5))


def super_fun2(**kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return total

print(super_fun2(num1=5, num2=4))

#Excersice - Highest even, looks for the highest even number
def highest_even(li):
    li.sort()
    li.reverse()
    for number in li:
        if number % 2 == 0:
            return number
print(highest_even([10,2,3,4,8,11]))

# Walrus Operator - := Assigns values to variables as part of a larger expresion
a = "helloooooooooo"
if ((word_len := len(a)) > 10):
    print(f"too long {word_len} elements")
