import random
import copy

#Milan Labus SD2B

#Define a function that takes a list and int as params
def elimination_game(playerList, index):
    print(" Eliminated: "+playerList.pop(index))
    playerTuple = tuple(playerList)
    return playerTuple





#create a list of 12 players
players = []
n=12   #the number of players there will be
#Asking the user to fill the player lsit

for i in range(0, n):     #looping 12 times
    print("Enter a player: ")
    player =  input()   #creating the player the user wants
    players.append(player)

#copying original list
original_Players = copy.copy(players)





while True:
    try:
        # asking user for number of players to be removed this play
        playersToRemove = input("Enter Number of players to be removed(MAX 6): ")
        if int(playersToRemove) < 2 or int(playersToRemove) > 6:    #raise error if input is out of bounds
            raise ValueError
        break
    except ValueError:
        print("Error please enter a number between 2 and 6")



for _ in range(int(playersToRemove)):       #loop the user specified number of times
    resultingTuple = (elimination_game(players,random.randint(1, 6)))    #Storing the returned Typle



print(" Result tuple: " + str(resultingTuple))


print(" Original List" + str(original_Players))