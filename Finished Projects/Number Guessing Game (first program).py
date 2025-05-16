# Number Guessing Game by ScribeShock
import random
number = random.randint(1,100)
guess = int(input("Choose Your Charact- Number...: "))
if guess > number:
    print(f"{guess} is too high, aim lower.")
elif guess == number:
        print(f"{guess} IS CORRECT, Here is your prize... Nothing! You Earned It!. :D")
elif guess < number:
    print(f" {guess} is too low, aim higher.")
else:
    print(f"try again")
