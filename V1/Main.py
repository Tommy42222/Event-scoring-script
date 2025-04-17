
teamScoreDict = {}
teamPlayerList = [[],[],[],[]]
playerScoreDict = {}

print("TEAM INTRO")

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
                
        print(teamPlayerList)
    break


