import random

print("Welcome to Python Number Guessing Game")
print("1. Start")
print("2. Exit")
choice = int(input("Enter your choice: "))

def number_guess() :
    # Generate a random number between 1 and 100
    global secret_number
    secret_number = random.randint(1, 100)
    
    # Set the number of attempts
    global max_attempts
    max_attempts = 10

    global attempts
    attempts = 0

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess between 1 - 100: "))
            
            # Increment the attempts
            attempts += 1
            if guess == secret_number:
                print("Congratulations! You guessed right number!")
                break
            elif attempts == max_attempts :
                print("Better luck next time :)")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return

if choice == 1 :
    number_guess()
elif choice == 2 :
    print("Exiting.................")
else :
    print("Enter right number!")