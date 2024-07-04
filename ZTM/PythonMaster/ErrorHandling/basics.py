# Error handling 
while True:
    try:
        age = int(input("What is your age?"))
        print(age)
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please Enter age higher than 0")
    else:
        print("Thank you! ")
        break

def sum(num1, num2):
    try:
        raise ValueError("Hey value error")
        return num1 + num2
    except TypeError as err:
        print("Please enter numbers: ",err)

    finally: # It will always run no matter what
        print("Okay I am finally done")


print(sum("1",2))
