import random
import math
from art import logo_list


print(random.choice(logo_list))
print("Welcome to the Number Guessing Game!")

# Safe integer input helpers
def input_int(prompt):
	while True:
		value = input(prompt)
		try:
			return int(value)
		except ValueError:
			print("Please enter a valid integer.")


# Read bounds with validation
while True:
	lower = input_int("Enter Lower bound:- ")
	upper = input_int("Enter Upper bound:- ")
	if lower > upper:
		print("Lower bound cannot be more than upper bound. Try again.")
		continue
	if lower == upper:
		print("Lower and upper are the same. Range will contain a single number.")
	break

# generating random number between the lower and upper
x = random.randint(lower, upper)

# Calculate attempts using ceiling of log2(range)
range_size = upper - lower + 1
max_attempts = max(1, math.ceil(math.log(range_size, 2)))
print("\n\tYou've only", max_attempts, "chances to guess the integer number!\n")

# Game loop
count = 0
guessed = False
while count < max_attempts:
	# taking guessing number as input (validated and within bounds)
	while True:
		guess_input = input("Guess a number: ")
		try:
			guess = int(guess_input)
		except ValueError:
			print("Please enter a valid integer.")
			continue
		if guess < lower or guess > upper:
			print(f"Out of range! Please guess between {lower} and {upper}.")
			continue
		break

	count += 1

	# Condition testing
	if x == guess:
		print("Congratulations you guessed it in", count, "try" if count == 1 else "tries")
		guessed = True
		break
	elif x > guess:
		print("You guessed too small!")
	else:
		print("You guessed too high!")

	remaining = max_attempts - count
	if remaining > 0:
		print(f"Attempts remaining: {remaining}\n")

# If not guessed within required guesses, reveal the number
if not guessed:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
