# Lambda Expresion - One time function expresions but you don't need anymore
#lambda param: action(param)
print(list(map(lambda item: item*2, [1,2,3,4,5])))

# Exercise: Lambda Expresions
# Square a list
my_list = [5,4,3]
my_list.sort()
my_list = list(map(lambda num: num**2,my_list))
print(my_list)

# List sorting 
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x:x[1])
print(a)
