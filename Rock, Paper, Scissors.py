import random
rock = "3"
scissors = "2"
paper = "1"

#counts for the outcomes and the while loop
count = 1
tieCount = 0
winCount = 0
loseCount = 0
while count != 4 and winCount < 2 and loseCount < 2:

#settings for the computer
    computerAnswer = str(random.randrange(1, 4))
    if computerAnswer == '1':
        computerAnswer = 'paper'
    elif computerAnswer == '2':
        computerAnswer = 'scissors'
    elif computerAnswer == '3':
        computerAnswer = 'rock'

#user input
    user = input("Enter your choice: ")
    print(computerAnswer)

#game rules
    if user == 'rock' and computerAnswer == 'scissors':
        print("You win!")
        winCount += 1
    elif user == 'scissors' and computerAnswer == 'paper':
        print("You win!")
        winCount += 1
    elif user == 'paper' and computerAnswer == 'rock':
        print("You win!")
        winCount += 1
    elif user == computerAnswer:
        print("Tie")
        tieCount += 1
        count-= 1
    else:
        print("You lose!")
        loseCount += 1
    count += 1
#print the outcomes
    print(f'\nWINS: {winCount}')
    print(f'\nLOSES: {loseCount}')
    print(f'\nTIES: {tieCount}')



#the ending of the game
print('\nGAME OVER')
if winCount > loseCount:
    print("\nUSER WINS!")
else:
    print("\nCPU WINS!")

