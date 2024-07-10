''' Given 2 arrays, create a function that let's a user know (true /false) whether
    these two arrays contain any common items
    For Example:
    const array1 = ['a','b','c','d']
    const array2 = ['z','b','x']
    return true
'''

def check_diff(list1, list2):
    hash = set()
    for item in list1:
        hash.add(item)
    for item in list2:
        if item in hash:
            return True
    return False

print(check_diff(['a','b','c','d'],['z','b','x']))
print(check_diff(['a','c','d'],['z','b','x']))