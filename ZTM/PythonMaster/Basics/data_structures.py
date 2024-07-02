# Lists - Mutable list of things
li = [1,2,3,4,5]
li2 = ["a","b","c","d"]
li3 = [1,2,"a",True]

print(li[0])
print(li2[1])
print(li3[3])

# List Slicing
amazon_cart = [
    "Notebooks",
    "Sunglasses",
    "Toys",
    "Grapes"
]

print(amazon_cart)

# Change List
amazon_cart[0] = "Laptop"
print(amazon_cart)

print(amazon_cart[-1])
# [start:stop:step]
print(amazon_cart[1:3:2])

# Matrix - Multidimensional Array (list)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Access 5
print(matrix[1][1])

# Methods
basket = [1,2,3,4,5]

#length 
print(len(basket))

#Adding
basket.append(6)
print(basket)

#Insert (specific position) .insert(position, value)
basket.insert(2,100)
print(basket)

# Extend - adds a list to the old one
basket.extend([100,200,300,400,500])
print(basket)

#remove - .pop(position) or pop() - removes the last item
basket.pop() #removes the 500 at the end
print(basket)

basket.pop(2) #it will remove the 100 in the middle
print(basket)

# remove - .remove(item) - you need to give it an item to remove not index
basket.remove(300)
print(basket)

# clear - removes all items from list
basket.clear()
print(basket)

# Index - returns the index of a value 
# .index(value,start,stop)
print(["a","b","c","d","e"].index("c"))
print(["a","b","c","d","e"].index("d",2))
print(["a","b","c","d","e"].index("d",2,4))

# Check if exists
print("f" in basket)

# Count - returns how many times it occurs
print(["a","b","c","c","d","c"].count("c"))

# Sort - Sorts in the values - Mutates the list to an ordered list
new_list = ["b","d","a","e","c","f","g"]
new_list.sort()
print(new_list)

#Sorted - Same as sort but doesn't mutate it
print(sorted(["b","d","a","e","c","f","g"]))

# Copy , copies the list
list_copy = new_list.copy()
print(list_copy)

# Reverse - reverse the items but does not sort it
new_list.sort()
new_list.reverse()
print(new_list)

# Join - Converts to string
new_string = "".join(["Hi","my","name","is","JOJO"])
print(new_string)

#Dictionary - Not sorted or order
dictionary = {
    "a":1,
    "b":"item",
    "c":False
}
print(dictionary["b"]) #It will print "item"

# Methods
dictionary2 = {
    "Player":"MezcalFighter",
    "Money":30000,
    "isActive":True
}

# .GET - Returns the value from the key if exists
print(dictionary2.get("Age")) #It will return none because Age does not exist

# Default value if does not exist
print(dictionary2.get("Age",27)) #It will return 27 because Age does not exist

dictionary3 = dict(Player="MezcalFighter")
print(dictionary3)

#Another method if exist
print("Player" in dictionary2) #True because the key exists

# Keys - Check if the keys exist
print("Age" in dictionary2.keys()) # False

# Value - Check if the value exist
print("MezcalFighter" in dictionary2.values()) # True

#Items - list the entire dictionary
print(dictionary2.items())

# Clear - Clears the dictionary
dictionary3.clear()
print(dictionary3)

# Copy - copies the dictionary
user = dictionary2.copy()
print(user)

#Pop - it removes the value from the key 
name = user.pop("Player")
print(name)
print(user) #Player is no longer in there because it was removed

# popitem - removes the key and the last value from the item
isActive = user.popitem()
print(isActive) # Prints ('isActive', True) because it has the key and the value

#Update - updates a key value or adds a new one
print(user.update({"Age":27}))
print(user)

# Tuple - Inmutable lists
my_tuple = (1,2,3,4,5)

new_tuple = my_tuple[1:3]
print(new_tuple)

# Methods
# Count - Index
print(my_tuple.count(5)) # Counts the times that 5 is in my_tuple
print(my_tuple.index(3)) # Find the index of 3

# Sets - Unorder collection of unique values
my_set ={1,2,3,4,5,6} # Cannot have duplicated values, if found then it overrides it
my_set.add(2)
print(my_set) # 2 was overrided in the same 2
my_set.add(100) 
print(my_set) # Adds 100 since there is no other

# Create a set based of a list with duplicates
ex_list = [1,2,3,4,5,5]
ex_set = set(ex_list) # the duplicate 5 won't be added since it cannot have duplicates
print(ex_set)

# Check if exists 
print(1 in my_set) # It will print True
print(900 in my_set) # It will print False

# Check the length of set
print(len(my_set))

# Copy set
new_set = my_set.copy()
print(new_set)

# Clears set
new_set.clear()
print(new_set)

# Different methods
diff_set = {1,2,3,4,5}
new_diff = {4,5,6,7,8,9,10}
# Difference - Looks for the difference
print(diff_set.difference(new_diff)) # 1,2,3 since 4 and 5 are in new_diff

# Discard - # Discard an item from set
diff_set.discard(5) 
print(diff_set) # it will print 1,2,3,4 since 5 was discarted

# Difference_update - Removes all elements of another set from this set
#diff_set.difference_update(new_diff) 
#print(diff_set) # it will print an empty set 

# intersection -
print(diff_set.intersection(new_diff)) # it will print only 4 since they only both have 4

# isdisjoint - # Returns true or false, true if they don't have something in common and false if they do
print(diff_set.isdisjoint(new_diff)) # false, they both have 4

# issubset - All contents of one set are in other set (subset)
print(diff_set.issubset(new_diff)) # False, they only have 4 in common

# issupperset - If the other set is the complete set of a subset
print(new_diff.issuperset(diff_set)) # False

# union - Concatenates both sets into one
print(diff_set.union(new_diff))