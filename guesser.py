
#!/usr/bin/env python3

#Guessing Game!

import random

def main():
	print("Guess a number between 1 and 100?")	
	print("You only get 5 chances!")
#	randomNumber = 11
	randomNumber = random.randint(1, 100)
	found = False
	count = 4

	while not found:
		userGuess = eval(input("Take a guess..."))
		
		if userGuess == randomNumber:
			print("You got it! Congrats!!! And you had {} chances left tool!".format(count))
			found = True
		elif userGuess > randomNumber and count >=1:
			print("Guess lower...and you have {} chances left".format(count))
		elif userGuess < randomNumber and count >=1:
			print("Guess higher..and you have {} chances left".format(count))
		
		if count == 0:
			print("Game Over...SORRY!")
			print("The answer was {}".format(randomNumber))
			break

		count -=1


if __name__ == "__main__":
	main()


