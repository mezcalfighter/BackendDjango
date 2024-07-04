# Generators - Allows us to create a sequence over time (an iterable)
# range - generator
# list - not a generator

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

# Yield
def generator_function(num):
    for i in range(num):
        yield i*2 #paused the function until we do something to it

g = generator_function(100)
next(g) #0 Called a first time -  0 * 2
next(g) #2 called a second time 1 * 2
print(next(g)) #4  because it will be used only every time it is called with next()
print(next(g)) #6 called again 3 * 2