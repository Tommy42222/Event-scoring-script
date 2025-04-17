#tracks each teams score
teamScoreDict = {}

# tracks the names of players in each team
teamPlayerList = [[],[],[],[]]

# tracks the scores for each solo player
playerScoreDict = {}

# holds the academic and sporty TEAM events
teamEventList = [["Pub Quiz", "Treasure hunt"],["Football", "Rounders", "Relay"]]

# holds the academic and sporty SOLO events
soloEventList = [["Spelling bee","Treasure hunt"],["Sack race", "Running", "Egg and Spoon race"]]

# tracks the SOLO players taking part in each event
eventPlayersList=[[],[],[],[],[]]

teamPoints = [15,10,8,4]

soloPoints = [15, 12,10, 8, 6, 3]


print(teamEventList)
print(soloEventList)

print("TEAM INTRO")
# NOTE COMMENT CODE BACK IN LATER
# # whle loop for adding each team and asigning their players
# while True:

#     # Loops for each team
#     for teamNumber in range(1,5):
#         print(f"ADDING PLAYERS TO TEAM {teamNumber}")
        
#         # Loops for each player in team
#         for playerNumber in range(1,6):

#             # loops untill valid player is added to team
#             while True:

#                 userInput = input(f"Enter the name for player {playerNumber} >>> ")
                
#                 # validates input:
#                 # NOTE Add more and propper validation later

#                 if userInput in teamPlayerList[int(teamNumber)-1]:
#                     print("entered name is already in list, please try again")
               
#                 elif userInput == "":
#                     print("Please enter a players name, please try again")

#                 else:
#                     teamPlayerList[int(teamNumber)-1].append(userInput)
#                     break
        
#         print(f"Members of team {teamNumber} are: {teamPlayerList[int(teamNumber)-1]} \n\n\n")
#     break


counter = 0
# user enters players for solo events
while True:

    if counter == 20:
        print("Max number of players added... moving on")
        break

    userInputplayer = input(f"\n--\nEnter the name of player No.{counter + 1} >>> ")

    # checks if stop command is given and if 5 or more players are added, if yes, break
    if userInputplayer == "stop" or userInputplayer == "-":
        if counter < 5:
            print("At least 5 players must be added before moving on... Please try again\n")
            print(f"you have entered {counter} Players, you need at least 5 to move on\n\n")

        else:
            print("stop commaned detected, moving on...")
            break

    # Same validation as the last section
    elif userInputplayer in playerScoreDict:

        print(f"A player called {userInputplayer} already exists, please try again")

    elif userInputplayer == "":
        print("Please enter a players name, please try again")

    else:
        playerScoreDict[userInputplayer] = 0



        # user selects which events the newly added player will take part in
        while True:
            userInputEvent = input("\n1-5 = single event, '' = all solo events >>> ")
            
            # if user selected all events, add player to all event lists and print result
            if userInputEvent == "":
                for i in range(len(eventPlayersList)):
                    eventPlayersList[i].append(userInputplayer)

                break
            
            #else if user entered value between 1 and 5, add player to event list at index
            elif int(userInputEvent) >0 and int(userInputEvent) <6:
                
                eventPlayersList[int(userInputEvent)-1].append(userInputplayer)
                break

            
            else:
                print("INVALID INPUT")

        counter += 1


