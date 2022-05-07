import random

print("ROCK!")
print("PAPER")
print("SCISSORS!")

p1 = input("Choose your weapon: ")
p1 = p1.lower()

pc = random.randint(1, 3)
if pc == 1:
	pc = "rock"
	print("computer plays: ROCK")
elif pc == 2:
	pc = "paper"
	print("computer plays: PAPER")
else:
	pc = "scissors"
	print("computer plays: SCISSORS")


if p1 == pc:
	print("IT'S A TIE!")
elif p1 == "rock" and pc == "paper":
	print("COMPUTER WINS!")
elif p1 == "rock" and pc == "scissors":
	print("PLAYER 1 WINS")
elif p1 == "paper" and pc == "scissors":
	print("COMPUTER WINS!")
elif p1 == "paper" and pc == "rock":
	print("PLAYER 1 WINS")
elif p1 == "scissors" and pc == "rock":
	print("COMPUTER WINS!")
elif p1 == "scissors" and pc == "paper":
	print("PLAYER 1 WINS")
else:
	print("Standard rules only :(")