import sys
import random
from enum import Enum

game_count = 0



def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\n Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1,2 or 3")
        return play_rps()

    player = int(playerchoice)

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose "+ str(RPS(computer)).replace("RPS.", "") + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return"✌🏿You win! "
        elif player == 2 and computer == 1:
            return"✌🏿You win!"
        elif player == 3 and computer == 2:
            return"✌🏿You win!"
        elif player == computer:
            return"😛Tie game!"
        else:
            return"🐍Python wins!"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print(f"\n Game count: {game_count}")

    print("\n Play again?")

    while True:
        playagain = input("\n Y for Yes or \nQ for Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n 🎉")
        print("Thank you for playing! \n")
        sys.exit("Bye!")


play_rps()