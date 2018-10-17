#get the random module which returns an unexpected value within specified range
import random
print("This is a simple rock paper scissor game ")
p1s=0
p2s=0
while True:
	print("Enter your choice \n1.Rock\n2.Paper\n3.Scissor\n")
	#its takes player1 input
	take1=int(input("enter your choice of 1,2,3 : "))
	if take1 == 1:
		p1take = "Rock"
	elif take1 == 2:
		p1take = "Paper"
	else:
		p1take = "Scissor"
	print("Player1 choice is ",p1take)
	#player2 input is taken randomly
	print("\nIts palyer2 turn  ")
	#the randint function return pseudorandom integer between the range
	take2 = random.randint(1,3)
	while take2 == take1:
		take2 = random.randint(1,3)
	if take2 == 1:
		p2take = "Rock"
	elif take2 == 2:
		p2take = "Paper"
	else:
		p2take = "Scissor"
	print("\nPlayer2 choice is ",p2take) 
	print("\n",p1take, "v/s" ,p2take)
	#game theme
	if((take1 == 1 and take2 == 2) or (take1 == 2 and take2 == 1)):
		res = "Paper"
	elif((take1 == 1 and take2 == 3) or (take1 == 3 and take2 == 1)):
		res = "Rock"
	else:
		res = "Scissor"
	#result declaration
	if res == p1take:
		print("\nPlayer1 wins ")
		p1s=p1s+1
	elif res == p2take:
		print("\nPlayer2 wins ")
		p2s=p2s+1
	else:
		print("\nIts a tie ")
	print("\nDo you want to play again?(Y/N)")
	ans = input()
	if ans == 'n' or ans == 'N':
		break
#get the score of the players and declare winner
print("score of player1 is ",p1s)
print("score of player2 is ",p2s)
if p1s>p2s:
	print("player1 is winner")
elif p2s>p1s:
	print("Player2 is winner")
else:
	print("its a tie ")
print("\nThanks for playing")

		
		
