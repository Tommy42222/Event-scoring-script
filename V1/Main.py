#tracks each teams score
teamScoreDict = {"team1":0,"team2":0,"team3":0,"team4":0}

teamPlacementList = []
# tracks the scores for each solo player
playerScoreDict = {"a":0, "b":0,"c":0,"d":0,"e":0,"g":0,"z":0}

playerPlacementList = []
# tracks the names of players in each team
teamPlayerList = [[],[],[],[]]

# tracks the SOLO players taking part in each event
eventPlayersList=[["a","e","d","b","c",],["a","e","d","b","c","g"],["a","e","d","b","c","z"],["a","e","d","b","c","g"],["a","e","b","c",]]
# how many points will be awarded to each team based on their placement
teamPoints = [15,10,8,4]
# how many points will be awarded to each solo player based on their placement
soloPoints = [15,12,10, 8, 6, 3]




###################################==-- ADD TEAMS AND THEIR PLAYERS --==########################################################################

print("TEAM INTRO")

# NOTE COMMENT CODE BACK IN LATER

# whle loop for adding each team and asigning their players
# while True:

#     # Loops for each team
#     for teamNumber in range(1,5):
#         # create a team and store in the dict
#         teamScoreDict[f"team-{teamNumber}"] = 0

#         print(f"ADDING PLAYERS TO TEAM {teamNumber}")
        
#         # Loops for each player in team
#         for playerNumber in range(1,6):

#             # loops untill valid player is added to team
#             while True:

#                 userInput = input(f"Enter the name for player {playerNumber} >>> ")
                
#                 # validates input:
#                 # NOTE Add more and propper validation later TOM!!!

#                 if userInput in teamPlayerList[int(teamNumber)-1]:
#                     print("entered name is already in list, please try again")
               
#                 elif userInput == "":
#                     print("Please enter a players name, please try again")

#                 else:
#                     teamPlayerList[int(teamNumber)-1].append(userInput)
#                     break
#         #prints out the team and all of its members
#         print(f"Members of team {teamNumber} are: {teamPlayerList[int(teamNumber)-1]} \n\n\n")
#     break


######################################==-- ADD SOLO PLAYERS AND ASIGN THEM EVENTS --==########################################################################

# # NOTE add player section starts here


counter = 0

#prints instructions of the different commands to the screen 
commands = "\n>>> Special Commands <<<\n\n. '-pl' = print out 5 lists each containg the players taking part in that event\n. " \
"'-stop', or '--' stops adding new players and moves on to event selction. NOTE: this can only happen if each event has AT LEAST 5 Participant" \
"\n. '-help' prints these instructions again"
print(commands)

while True:
    # if 20 players have been added, brack and move onto event selection
    if counter == 20:
        print("Max number of players added... moving on")
        break

    # prompts the user for input
    userInputplayer = input(f"\n--\nEnter the name of player No.{counter + 1} >>> ")

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
        for event in eventPlayersList:
            print(f" Event {count + 1} - {eventPlayersList[count]}")
            count += 1

    elif userInputplayer == "-help":
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
                 [["pass","piss"],["balls","snogging","rim-job"]], # Solo events
                 [["dick","fucking"],["kissing on your sister","kicking me in the balls","dying"]]  # Team events
                 ]

# turns the solo events into a flat 1d-list, this is so the right players take part in the right event
flattenedSoloEventsList = [item for sublist in EventsList[0] for item in sublist]




    
while True:
    # counts the number of items in the 4 lists, once it == 0, break and move on
    numberOfEventsInList = len(EventsList[0][0] + EventsList[0][1] + EventsList[1][0] + EventsList[1][1])

    if numberOfEventsInList == 0:
        print("all events ran, bracking loop")
        break

    while True:

        
        userInput = int(input("1 = Solo\n2 = Team\n>>> "))
        
    
        # if there are accedemic events left for the selected group, show those events
        if EventsList[userInput-1][0] != []:
            print("showing all avliable acedemic items in list\n")
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
        


    # user is prompted to select an event from the list of outputs
    userInputEvent = input((f" Here is your list of avaliable options to select from:\n{output}\n>>> "))

    # if user put is valid, remove the option from the list and asign it to "selectedEvent"
    if userInputEvent in output:
        selectedEvent = userInputEvent
        print(f"Removing {userInputEvent}")
        output.remove(userInputEvent)
       
    else:
        print("Invalid selection, please try again")

#####################################==-- Solo event placement --==###################################################################           
    
    # try and get the index if a solo event, will throw an error if team event
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
                userInputPlayerSelect = input(f"Which player came in {i} Position?\n>>> ")
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

#####################################==-- Team event placemen --==###################################################################    
    else:
        print(f"The next TEAM event is {selectedEvent}!")

        # run block for each of the 4 teams
        for i in range(1,5):
            while True:
                userInputTeamSelect = input(f"Which team came in {i} Position?\n>>> ")
                # check if team is in that events list, and has not already been awarded a position already
                if userInputTeamSelect in teamScoreDict.keys() and userInputTeamSelect not in teamPlacementList:
                    #if team is valid, add the relvant amount of points to their key-value pair in the dictionary, and add them to the list so they cant be awarded a position again
                    teamScoreDict[userInputTeamSelect] = teamScoreDict.get(userInputTeamSelect, 0) + teamPoints[i-1]                    
                    teamPlacementList.append(userInputTeamSelect)
                    break


        teamPlacementList = []
       
        print(f"--> TEAM SCORES AFTER THE {selectedEvent} EVENT <--\n{teamScoreDict}")
print("this is the end")


