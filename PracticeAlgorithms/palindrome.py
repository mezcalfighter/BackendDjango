def palindrome_check(new_item,old_item):
    if new_item == old_item:
        return True
    return False

def reverse_item(item):
    new_item = item[-1::-1]
    return palindrome_check(new_item, item)

print(reverse_item("anna"))
print(reverse_item("emanuel"))