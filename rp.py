from random import randint

t = ["Rock", "Paper", "Scissors"]
print("Welcome to the good old game of Rock,Paper,Scissors!\n")
player_name = input("Enter your name: ")

player_wins = 0
computer_wins = 0


while True:

    computer_index = randint(0, 2)
    computer = t[computer_index]

   
    player = input("Rock, Paper, Scissors? (Type 'end game' to finish)\n -" ).capitalize()

   
    if player == 'End game':
        break

   
    if player not in t:
        print("That's not a valid play. Check your spelling!")
        continue

    
    print("Computer chooses:", computer)

   
    if player == computer:
        print("Tie!")
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        print("You win!", player, "beats", computer)
        player_wins += 1
    else:
        print("You lose!", computer, "beats", player)
        computer_wins += 1


print("Final Result: You -", player_wins, "Computer -", computer_wins)

if player_wins > computer_wins:
    print("Congratulations,", player_name + "! You Won!")
elif player_wins < computer_wins:
    print("Sorry,", player_name + ", you lost. Better luck next time!")
else:
    print("It's a tie,", player_name + "! Nobody wins.")
