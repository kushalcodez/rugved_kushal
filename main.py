import random
def userin():
    player_choice=input("enter choice rock paper or scissors \n")
    options=["rock","paper","scissors"]
    computer_choice = random.choice(options)
    dict={"player":player_choice,"computer":computer_choice}
    return dict
def checkwin(player,computer):
    print(f"you chose {player} \ncomputer chose {computer}")
    if player==computer:
        return "its a tie"
    elif player=="rock":
        if computer=="scissors":
            return "ROCK SMASHES SCISSORS YOU WIN"
        else:
            return "PAPER CATCHES ROCK YOU LOSE"
    elif player=="paper":
        if computer=="scissors":
            return "SCISSORS CUTS PAPER YOU LOSE"
        else:
            return "PAPER CATCHES ROCK YOU WIN"
    elif player=="scissors":
        if computer=="rock":
            return "ROCK SMASHES SCISSORS YOU LOSE"
        else:
            return "SCISSORS CUTS PAPER YOU WIN"
choices=userin()
result=checkwin(choices["player"],choices["computer"])
print(result)
    
    