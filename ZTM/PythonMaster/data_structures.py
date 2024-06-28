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