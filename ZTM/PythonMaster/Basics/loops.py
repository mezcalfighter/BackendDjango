# Excercise - Counter list 
numbers = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for number  in numbers:
    counter += number
print(counter)

# Range - given a number it will create a sequence
# range(start, stop, step) - range(start, stop) - range(number)
for number in range(0,10,2):
    print(number)

# Enumerate - gives an index number on each item of an object
for number,char in enumerate("Hellooooooo"):
    print(number, char)

# Excercise - Print image
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            text = " "
            print(" ",end="")
        else:
            print("*",end="")
    print("")

# Check duplicates
some_list = ["a","b","c","b","d","m","n","n"]
new_list = []
duplicates = []
for char in some_list:
    if char in new_list:
        duplicates.append(char)
    else:
        new_list.append(char)
if duplicates:
    print(duplicates)
    print("Your list has duplicates")