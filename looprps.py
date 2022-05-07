from random import randint
print('ROCK!')
print('PAPER!')
print('SCISSORS!!!!')
pscore=0
cscore=0
while True:
	print(f"Current Score - Player: {pscore} PC: {cscore} ")
	player = input("CHOOSE YOUR WEAPON: ").lower()
	rng = randint(0,2)
	if (rng == 0):
		pc = "rock"
	elif (rng == 1):
		pc = "paper"
	else:
		pc = "scissors"

	print(f"Computer counters with: {pc}")

	if player == pc:
		print("OH MY ITS A TIE")
	elif player == "rock":
		if pc == "paper":
			print("COMPUTER WINS!!")
			cscore+=1
		else:
			print("YOU WIN!!")
			pscore+=1
	elif player == "scissors":
		if pc == "rock":
			print("COMPUTER WINS!!")
			cscore+=1
		else:
			print("YOU WIN!!")
			pscore+=1
	elif player == "paper":
		if pc == "scissors":
			print("COMPUTER WINS!!")
			cscore+=1
		else:
			print("YOU WIN!!")
			pscore+=1
	if pscore==(cscore+2):
		retry=input("YOU WIN BEST TWO OUT OF THREE! Play again? y/n ")
		if retry == "y":
			pscore, cscore=0, 0
		else:
			print("thanks for playing")
			break
	elif cscore==(pscore+2):
		retry=input("you lose...try again? y/n")
		if retry == "y":
			pscore, cscore = 0, 0
		else:
			print("Thanks for playing!")
			break


	
