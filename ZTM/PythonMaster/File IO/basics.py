# Reading files
my_file = open("test.txt")
print(my_file.read())
my_file.seek(0) # Reset cursor to the given location (the start)
print(my_file.readline()) # Reads only the line where the cursor is
print(my_file.readlines()) # Returns a list with each line the doc has

# You must close the file after you're done
my_file.close()


# Easiest way to read files qwithout worrying on closing the file
with open("test.txt", mode="a+") as my_file:
    my_file.write("Hey it\'s me!")
    print(my_file.readlines())