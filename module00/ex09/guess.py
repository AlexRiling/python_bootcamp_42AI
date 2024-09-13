import random

def guess(random_number: int):
    print("""
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
"""
    )
    attempts = 0
    while True:
        try:
            user_input = input("What's your guess between 1 and 99?\n>> ")

            # Allow user to exit by typing 'exit'
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Convert input to integer
            number = int(user_input)

            attempts += 1

            if random_number == number:
                print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
                break
            elif random_number < number:
                print("Too high!")
            else:
                print("Too low!")

        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break


def main():
    number = random.randint(1, 99)  # Note: randint(1, 99) includes 1 and 99
    try:
        guess(number)
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")


if __name__ == "__main__":
	main()
