#tracks each teams score
teamScoreDict = {}

# tracks each teams name
teamNameList = []

# makes sure a team can't come in 2 places in 1 event
teamPlacementList = []

# tracks the names of players in each team
teamPlayerList = [[],[],[],[],[]]

# tracks the scores for each solo player
playerScoreDict = {}

# makes sure a player can't come in 2 places in 1 event
playerPlacementList = []

# tracks the SOLO players taking part in each event
eventPlayersList=[[],[],[],[],[]]
# how many points will be awarded to each team based on their placement
teamPoints = [15,10,8,4]

# how many points will be awarded to each solo player based on their placement
soloPoints = [15,12,10, 8, 6, 3]

placasementPrefixes = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th",
                       "11th","12th","13th","14th","15th","16th","17th","18th","19th","20th"]




###################################==-- ADD TEAMS AND THEIR PLAYERS --==########################################################################

print("TEAM INTRO")
counter = 0
teamName = 0
# NOTE COMMENT CODE BACK IN LATER

# whle loop for adding each team and asigning their players
while True:

    # Loops for each team
    for teamNumber in range(1,5):


        while True:
            teamNameInput = input("What name do you want to give this team: If you want a defult name, leave this blank and hit enter\n>>> ")

            if teamNameInput ==  "":
                teamName = f"Team-{teamNumber}"
                teamScoreDict[f"TEAM-{teamNumber}"] = 0
                break

            else:
                teamName = teamNameInput
                teamScoreDict[teamName] = 0
                break



        # create a team and store in the dict
        

        print(f"ADDING PLAYERS TO {teamName}")
        
        # Loops for each player in team
        for playerNumber in range(1,6):

            # loops untill valid player is added to team
            while True:

                
                userInput = input(f"Enter the name for player {playerNumber} >>> ")
                

                


                # validates input:
                # NOTE Add more and propper validation later TOM!!!
                
                if userInput in teamPlayerList[int(teamNumber)-1]:
                    print("entered name is already in list, please try again")
               
                elif userInput == "":
                    print("Please enter a players name, please try again")

                else:
                    teamPlayerList[int(teamNumber)-1].append(userInput)
                    

                    while True:
                        userInputEvent = input("\n1-5 = single event, 6 = all solo events,  = no solo events >>> ")
                        
                        # if user selected all events, add player to all event lists and print result
                        if userInputEvent == "":
                            break

                        elif int(userInputEvent) == 6:
                            for i in range(len(eventPlayersList)):
                                eventPlayersList[i].append(userInput)
                                playerScoreDict[userInput] = 0
                            break
                        
                        #else if user entered value between 1 and 5, add player to event list at index
                        elif int(userInputEvent) >0 and int(userInputEvent) <6:
                            
                            eventPlayersList[int(userInputEvent)-1].append(userInput)
                            playerScoreDict[userInput] = 0
                            break


                        else:
                            print("INVALID INPUT")

                            break
                    break
        #prints out the team and all of its members
        print(f"Members of team {teamNumber} are: {teamPlayerList[int(teamNumber)-1]} \n\n\n")
    break


######################################==-- ADD SOLO PLAYERS AND ASIGN THEM EVENTS --==########################################################################

# # NOTE add player section starts here




#prints instructions of the different commands to the screen 
commands = "\n>>> Special Commands <<<\n\n. '-pl' = print out 5 lists each containg the players taking part in that event\n. " \
"'-stop', or '--' stops adding new players and moves on to event selction. NOTE: this can only happen if each event has AT LEAST 5 Participant" \
"\n. 'help' prints these instructions again"
print("\n\n====- ADDING SOLO PLAYERS -====")
print(commands)

while True:
    # if 20 players have been added, brack and move onto event selection
    if counter == 20:
        print("Max number of players added... moving on")
        break

    # prompts the user for input
    userInputplayer = input(f"\n----\nEnter the name of player No.{counter + 1} >>> ")

    # checks a stop command is given
    if userInputplayer == "-stop" or userInputplayer == "--":
        # checks if each event has at least 5 players, if yes, break and move on
        if all(len(sublist) >= 5 for sublist in eventPlayersList):
        
            print("stop commaned detected, moving on...\n\n\n\n\n")
            break

        else:
            print("At least 5 players must be added before moving on/there must be AT LEAST 5 Players for EACH event... Please try again\n")
            print(f"you have entered {counter} players total\n")
            print(eventPlayersList)

    # prints each event and its players out on a new line
    elif userInputplayer == "-pl":
        count = 0
        print("====- PRINTING LIST -====\nREMEMBER, you need AT LEAST 5 players for each event")
        for event in eventPlayersList:
            print(f" Event {count + 1} - {eventPlayersList[count]}" + f" Count = {len(eventPlayersList[count])}")
            count += 1
    
    # command to remove and replace a player form both teams and solo events
    elif userInputplayer == "-rm":
        splitText = userInputplayer.split("|")
        while True:

            userInputFind = input("Who do you want to replace?\n>>> ")

            if  userInputFind in playerScoreDict:
                
                userInputReplace = input("Who do you want to replace them with?")

                if userInputReplace not in playerScoreDict:
                    
                    for i, sublist in enumerate(eventPlayersList):
                        for j, item in enumerate(sublist):
                            if item == userInputFind:
                                eventPlayersList[i][j] = userInputReplace
                
                    

                else:
                    print(f"{userInputReplace} already exists, plaese try another replacement name")
                
                for i, sublist in enumerate(teamPlayerList):
                        for j, item in enumerate(sublist):
                            if item == userInputFind:
                                teamPlayerList[i][j] = userInputReplace

               
                if userInputFind in playerScoreDict:
                    playerScoreDict[userInputReplace] = playerScoreDict.pop(userInputFind)
                    
                print(f"Removing {userInputFind} and replacing with {userInputReplace}")
                 




    # prints commands instructions again
    elif userInputplayer == "help":
        print(commands)

    # Same validation as the last section
    elif userInputplayer in playerScoreDict:

        print(f"A player called {userInputplayer} already exists, please try again")

    elif userInputplayer == "":
        print("Please enter a players name and please try again")





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


#######################################==-- EVENT SELECTION --==############################################################

# holds the diiffernt events for team and solos, first academic is solo, second is sporty
EventsList = [
                 [["spelling bee","treasure hunt"],["running","treasure hunt","sack race"]], # Solo events
                 [["pub quiz","treasure hunt"],["football","rounders","relay"]]  # Team events
                 ]

# turns the solo events into a flat 1d-list, this is so the right players take part in the right event
flattenedSoloEventsList = [item for sublist in EventsList[0] for item in sublist]




print("====- EVENT SELECTION -====\n")
while True:
    # counts the number of items in the 4 lists, once it == 0, break and move on
    numberOfEventsInList = len(EventsList[0][0] + EventsList[0][1] + EventsList[1][0] + EventsList[1][1])

    if numberOfEventsInList == 0:
        print("all events ran, bracking loop")
        break

    while True:

        
        userInput = int(input("1 = Solo\n2 = Team\nPLEASE ENTER 1 or 2\n>>> "))
        
    
        # if there are accedemic events left for the selected group, show those events
        if EventsList[userInput-1][0] != []:
            print("\nshowing all avliable acedemic items in list\n")
            output = EventsList[userInput-1][0]
            eventType = userInput
            break

        else:

            # else if selected group's accedemic events are empty, check if the other groups events are empty as well, 
            if EventsList[userInput % 2][0] == []:
                
                
                # If one group has completed all their events, show the sporty events for the other group
                if EventsList[userInput-1][1] == []:
                    print("This group have performed all their events. But, there are still events in the other group")
                    output = EventsList[userInput % 2][1]
                    eventType = (userInput + 1) % 2
                    break
        
                else:
                    # however, if there are still sporty events left in the selected group, show them to user
                    print("Showing sporing events for selected group\n")
                    output = EventsList[userInput-1][1]
                    eventType = userInput
                    break
        
            # otherwise, show the accedemic events for the other group
            else:    
                print("acmd empty: here are the remainging acmd events in the other group\n")
                output = EventsList[userInput % 2][0]
                eventType = (userInput + 1) % 2
                break
        


    while True:
        # user is prompted to select an event from the list of outputs
        userInputEvent = input((f" Here is your list of avaliable options to select from:\n\n{output}\nPlease type in the event you want to run, and hit ENTER\n>>>  "))
        selectedEvent = userInputEvent
        # if user put is valid, remove the option from the list and asign it to "selectedEvent"
        if userInputEvent in output:
            selectedEvent = userInputEvent
            print(f"Removing {userInputEvent}")
            output.remove(userInputEvent)
            break
        
        else:
            print("Invalid selection, please try again")

#####################################==-- Solo event placement --==###################################################################           
    
    # try and get the list contating the players for that event if it is a solo event, 
    # will do nothing if it is a team event
    try:
        eventIndex = flattenedSoloEventsList.index(userInputEvent)
    except ValueError:
        pass
    else:
        print(eventPlayersList[eventIndex])


    if eventType == 1:
        print(f"The next SOLO event is {selectedEvent}!")

        # run block for the top 5 placements
        for i in range(1,6):
            while True:
                userInputPlayerSelect = input(f"Which player came in {placasementPrefixes[i-1]} Position?\n>>> ")
                # check if player is in that events list, and has not already been awarded a position already
                if userInputPlayerSelect in eventPlayersList[eventIndex] and userInputPlayerSelect not in playerPlacementList:
                    # if player is valid, add the relvant amount of points to their key-value pair in the dictionary, and add them to the list so they cant be awarded a position again
                    playerScoreDict[userInputPlayerSelect] = playerScoreDict.get(userInputPlayerSelect, 0) + soloPoints[i-1]
                    playerPlacementList.append(userInputPlayerSelect)
                    break

                else:
                    print(f"Player {userInputPlayerSelect} does not exist, please try again\n")

        # if a player did not come in the top 5, award them 3 points
        for player in playerScoreDict.keys():
            if player not in playerPlacementList:
                playerScoreDict[player] = playerScoreDict.get(player, 0) + 3
        
        #reset the placment list
        playerPlacementList = []

        print(f"--> PLAYER SCORES AFTER THE {selectedEvent} EVENT <--\n{playerScoreDict}")

####################################==-- Team event placement --==###################################################################    
    else:
        
        print(f"The next TEAM event is {selectedEvent}!")

        listOfTeams = list(teamScoreDict.keys())
        
        
        counter = 1
        print("List of Teams")
        for team in listOfTeams:
            print(f"{team} = {counter}")
            counter += 1


        # run block for each of the 4 teams
        for i in range(1,5):
            while True:
                
                # input is an int between 1 and 4, is used to retrive the teams name from the listOfTeams list
                userInputTeamSelect = int(input(f"Which team came in {placasementPrefixes[i-1]} Position?\nPLEASE ENTER 1,2,3 or 4\n>>>  "))
                selectedTeam = listOfTeams[userInputTeamSelect-1]

                # check if team is in that events list, and has not already been awarded a position already
                if selectedTeam in teamScoreDict.keys() and selectedTeam not in teamPlacementList:
                    #if team is valid, add the relvant amount of points to their key-value pair in the dictionary, and add them to the list so they cant be awarded a position again
                    teamScoreDict[selectedTeam] = teamScoreDict.get(selectedTeam, 0) + teamPoints[i-1]                    
                    teamPlacementList.append(selectedTeam)
                    break


        teamPlacementList = []
       
        print(f"--> TEAM SCORES AFTER THE {selectedEvent} EVENT <--\n{teamScoreDict}")


#####################################==-- FINAL RESULTS DISPLAY (TEAMS) --==###################################################################    


# this sorts the teamScoreDict based on each teams score
sorteddict = sorted(teamScoreDict.items(), key= lambda x:x[1], reverse=True)
convertdict = dict(sorteddict)

# creates the centerd text that says who the winner is
#the winner is the first item pair in the sorted dict
Winner = list(convertdict.keys())[0]
Winner = f"{Winner} WINS!"
centeredWinner = Winner.center(50)

# creates the centerd Title for the team results
title = "FINAL RESULTS FOR THE TEAM EVENTS"
centeredTitle =title.center(50,"-")
print(centeredTitle)

# for each team in the sorted dict, give them a placement, print their name out, and state how many points they got
counter = 0
for player,AmountOfpoints in convertdict.items():
    print(f"{placasementPrefixes[counter]}: {player} got {AmountOfpoints} points")
    counter += 1
	
# print the centerd text that says who the winner is
print(f"\n{centeredWinner}\n\n")  


#####################################==-- FINAL RESULTS DISPLAY (SOLOS) --==###################################################################    

# NOTE all major functions in this section are the same as the team section above, 
# the only differnce is that this section references different dicts and lists

sorteddict = sorted(playerScoreDict.items(), key= lambda x:x[1], reverse=True)

convertdict = dict(sorteddict)

Winner = list(convertdict.keys())[0]
Winner = f"{Winner} WINS!"
centeredWinner = Winner.center(50)


title = "FINAL RESULTS FOR THE SOLO EVENTS"
centeredTitle =title.center(50,"-")


print(centeredTitle)


counter = 0
for player,AmountOfpoints in convertdict.items():
    print(f"{placasementPrefixes[counter]}: {player} got {AmountOfpoints} points")
    counter += 1
	
print(f"\n\n{centeredWinner}")  

print("END OF PROGRAM")
print(("="*50))













