import random

continue_app = True
while continue_app != "n":
    continue_app = input("Roll the dice? (y/n):").lower()
    if continue_app == "y":
        rand_num1 = random.randint(1,6)
        rand_num2 = random.randint(1,6)
        print(f"{rand_num1}, {rand_num2}")
    elif continue_app == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")
        break