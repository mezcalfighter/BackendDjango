import random
playing = True
number = random.randint(1,100)
while playing == True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess > 100 or  guess < 1:
            print("Number not in range")
        else:
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("Congratulations! You've found the number!")
                playing = False
                break
    except ValueError:
        print("Please enter a valid number")