import random
while True:
	num = random.randint(1,10)
	guess=input("What is your guess?: ")

	if num>10 or num<0:
		print("Nice try..1-10")

	while num != int(guess):
		print("Try again! ")
		guess=input()
	if num == int(guess):
		print("Correct!")
		retry=input("Play again? y/n ")
		if retry=="y":
			num = random.randint(1,10)
			guess=None
		else:
			print("Thanks for playing!")
			break