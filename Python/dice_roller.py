# Automatic Dice Roller
# Written by Owen McKenney

from random import randint

print("Automatic Dice Roller")
run = True

# while the run variable is true, the while loop will run
while run:
	i = str(input("Press enter to roll or x to quit: ")) # this gets the user's input
	if i == "":
		print(randint(1,6)) # prints a random number between 1 and 6
	elif i == "x":
		run = False # if input is "x", run = False
	else:
		print("error") # if input isn't an "x" or enter, prints error
		run = False

