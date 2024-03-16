import random


def roll():
    minvalue = 1
    maxvalue = 6
    roll = random.randint(minvalue, maxvalue)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

maxscore = 100
playerscores = [0 for _ in range(players)]

while max(playerscores) < maxscore:
    for playeridx in range(players):
        print("\nPlayer number", playeridx + 1, "turn has just started!")
        print("Your total score is:", playerscores[playeridx], "\n")
        currentscore = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentscore = 0
                break
            else:
                currentscore += value
                print("You rolled a:", value)

            print("Your score is:", currentscore)

        playerscores[playeridx] += currentscore
        print("Your total score is:", playerscores[playeridx])

maxscore = max(playerscores)
winningidx = playerscores.index(maxscore)
print("Player number", winningidx + 1,
      "is the winner with a score of:", maxscore)