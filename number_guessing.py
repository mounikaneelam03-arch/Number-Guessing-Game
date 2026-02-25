import random
number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts =0
while True:
    guess= int(input("Enter your guess: "))
    attempts += 1
    if guess<number:
        print("Too low! Try again")
    elif guess>number:
        print("Too high! Try again")
    else:
        print("Congratulations! You guessed the number")
        break
print(f"You guessed the number in {attempts} attempts.")
print("Thank you for playing!")