
def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    counter = 0
    while True:
        user_input = input("Enter the word 'apple': ")

        if user_input.lower() == "apple":
            # End the while loop
            break
        else:
            # Keep track of how many times the loop has run by incrementing the counter.
            # counter = counter + 1;
            counter += 1

    print(f"Thanks for entering 'apple' after {counter} tries")


# Puzzle A - Knock, Knock
# Write a knock, knock joke using while loops
#   "Knock, Knock!: "
#       "who's there?"
#   "Phil.... :"
#       "phil who?"
#   "Phil Deez Nuts!"
# The user should be continually prompted until they enter "who's there" or "who is there?" and "phil who?"
# If the user enters the wrong reply 2 times, tell them to write "who is there?" or "phil who?"
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')


def example_b():
    print('\nExample B')
    print('~~~~~~~~~')

    # It's common to use "i" as the counter variable.
    i = 1
    # Have a total variable outside the while loop
    total = 0

    print("Please enter 3 numbers and I will add them together: ")

    while i < 4:
        user_input = int(input(f"{i}) Enter a number: "))

        # Increase the total count
        total = total + user_input

        # Increment the counter
        i += 1

    print(f"The total was: {total}")


# Puzzle B - While there's maths
# Write a program that asks the user for a number between 1 and 10, then display the number to the power of 2,3,4 and 5.
# "Enter a number: "   2
# "2 to the power of 2 is 4"
# "2 to the power of 3 is 8"
# ...
# Continually prompt the user to enter a number between 1 and 10.
# Think of how this would be done in an IF statement, then just do it in a while loop - while <if statement expression>
# Use pow() to do the power calculation.

def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~')


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    # Boolean Values are True or False (Yes or No)
    # Often used as ON/OFF flags for loops.

    is_active = True
    counter = 0

    # While is_active: is shorthand for while is_active == true:
    while is_active:
        if counter <= 5:
            print(f"This is loop {counter}")
            counter += 1
        else:
            print("Ending loop")
            # Set is_active flag to false, prevents the while loop re-running
            is_active = False
            counter = 0             # Reset the counter as well.

            # The while loop condition is evaluated at the beginning of each loop
            # So if there was code after the "isActive = false" it will still run.
            # It is not a break; statement.
            print("This still runs as there is no break statement.")


# Puzzle C - Contagious Laughter
# Write a program that maniacally laughs at the user, as long as the user keeps laughing.
# The program will say "Ha ha ha ha ha... " and if the user enters a string that contains "ha" the program will laugh again.
# Hint: look up the "in" keyword
# After laughing 3 times, the program should display "Ha ha???..." and if the user enters a string containing "ha" then keep laughing!
# Use a keepLaughing boolean value to continually re-run a while loop.
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')


if __name__ == '__main__':

    # Run the puzzles

    example_a()
    #puzzle_a()

    example_b()
    #puzzle_b()

    example_c()
    #puzzle_c()

