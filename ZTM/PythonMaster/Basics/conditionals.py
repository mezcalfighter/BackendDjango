# Ternary
# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed"  if is_friend else "not allowed to message"
print(can_message) # Message Allowed

#  is vs == 
# == checks if something is equal
print(True == 1) # True
print("" == 1) # False
print([] == 1) # False
print(10 == 10.0) # False - Wrong it truncates the float to int to compare
print([] == []) # True

# is - checks for equality in value (if the value in memory is the same)
print(True is 1) # False
print("" is 1) # False
print([] is 1) # False
print(10 is 10.0) # False 
print([] is []) # False
print(1 is 1) # True
print([1,2,3] is [1,2,3]) # False because they are in different memory locations