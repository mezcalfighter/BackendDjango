strings = ["a","b","c","d"]

# Push
strings.append("x")

# pop
strings.pop()

# Unshift - Adds item at the beggining of the array
strings.insert(0,"y")

# Splice - Removes or adds an item to a specific position
strings.pop(3) # Removes the item in position 3
strings.insert(3, "alien")

print(strings)