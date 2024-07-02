birth_year = input("What year were you born? \n")
print(f"Your age is: {2024 - int(birth_year)}")

username = input("Username: ")
password = input("Password: ")

print(f"Hey, {username} your password {"*" * len(password)} is {len(password)} letters long")