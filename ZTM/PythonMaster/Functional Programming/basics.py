# Functional Programming (Pure functions)
# Packaging code (separation of concerns)
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# Map, filter, zip and reduce
# Map - iterable, data  map(function, data)
def duplicate_num(num):
    return num * 2

print(list(map(duplicate_num,[1,2,3,4,5])))

# Filter 
def only_odd(num):
    return num % 2 != 0

print(list(filter(only_odd,[1,2,3,4,5,6,7,8,9])))

# Zip - two list and we would zip them together
my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list,your_list))) #(1,10),(2,20),(3,30)
