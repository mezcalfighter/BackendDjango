# Debugging pdb - Python Debugger
# Other ways to debug
# Linting  - IDE / editor can indentify before running code

#Using pdb
import pdb

def add(num1,num2):
    print(num1, num2)
    pdb.set_trace()
    return num1+num2

add(4,"add")

# Commands for pdb, 
# List - Gives the documentation
# step - Go to the next line
# continue - Continues until it returns something
# a - returns all arguments
# w - shows the context of the current line
# exit - exits pdb
