from random import randint

wins = 0
for x in range(0,2):
    plays = ["Rock","Paper","Scissors"]

    computer = plays[randint(0,2)]

    win = False

    while win == False:
        player = raw_input().capitalize()
        if player == "Rock":
            if computer== "Paper":
                print("Computer Paper beats Player Rock")
                win = False
            else:
                wins +=1
                print("Player Rock beats Computer Scissors")
                win = True
        elif player == "Paper":
            if computer=="Scissors":
                print("Computer Scissors beats Player Paper")
                win = False
            else:
                wins +=1
                print("Player Paper beats Computer Rock")
                win = True
        elif player == "Scissors":
            if computer=="Rock":
                print("Computer Rock beats Player Scissors")
                win = False
            else:
                wins +=1
                print("Player Scissors beats Computer Paper")
                win = True
        elif player==computer:
            print("Draw")
        else:
            print("Invalid")

print("You have won " + wins + " out of 3 games")
