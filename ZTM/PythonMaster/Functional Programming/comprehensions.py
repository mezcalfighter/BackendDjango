# List Comprehesions, Set Comprehensions and Dictionary Comprehension
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)

# Same but using comprehencions
my_list = [char for char in "hello"]
print(my_list)

my_list2 = [num for num in range(0,100)]
print(my_list2)

my_list3 = [num*2 for num in range(0,100)]
print(my_list3)

my_list4 = [num*2 for num in range(0,100) if num % 2 == 0]
print(my_list4)

# Set Comprehension
my_set = {char for char in "hello"}
print(my_set)

my_set2 = {num for num in range(0,100)}
print(my_set2)

my_set3 = {num*2 for num in range(0,100)}
print(my_set3)

my_set4 = {num*2 for num in range(0,100) if num % 2 == 0}
print(my_set4)

# Dictionary Comprehensioins
simple_dict ={"a":1,"b":2}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

new_dict = {num:num*2 for num in [1,2,3]}
print(new_dict)

some_list = ["a","b","c","b","d","m","n","n"]
duplicates = list(set([item for item in some_list if some_list.count(item) == 2]))
print(duplicates)