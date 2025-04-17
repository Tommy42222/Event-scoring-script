#tracks each teams score
teamScoreDict = {}

# tracks the names of players in each team
teamPlayerList = [[],[],[],[]]

# tracks the scores for each solo player
playerScoreDict = {}

# holds the academic and sporty TEAM events
teamEventList = [[],[]]

# holds the academic and sporty SOLO events
playerEventList = [[],[]]

# tracks the SOLO players taking part in each event
eventPlayersList=[[],[],[],[],[]]


print("TEAM INTRO")

# whle loop for adding each team and asigning their players
while True:

    # Loops for each team
    for teamNumber in range(1,5):
        print(f"ADDING PLAYERS TO TEAM {teamNumber}")
        
        # Loops for each player in team
        for playerNumber in range(1,6):

            # loops untill valid player is added to team
            while True:

                userInput = input(f"Enter the name for player {playerNumber} >>> ")
                
                # validates input:
                # NOTE Add more and propper validation later

                if userInput in teamPlayerList[int(teamNumber)-1]:
                    print("entered name is already in list, please try again")
               
                elif userInput == "":
                    print("Please enter a players name, please try again")

                else:
                    teamPlayerList[int(teamNumber)-1].append(userInput)
                    break
        
        print(f"Members of team {teamNumber} are: {teamPlayerList[int(teamNumber)-1]} \n\n\n")
    break




