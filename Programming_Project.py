#// Imports //#
import random
import linecache
import time
import tkinter
import tkinter.font

#// Variables //#
points = 0
roundCounter = 0

artistsTxt = "Files\\Artists.txt"
authenticatedPlayersTxt = "Files\\AuthenticatedPlayers.txt"
doNotInputTxt = "Files\\DoNotInput.txt"
leaderboardTxt = "Files\\Leaderboard.txt"
lowercaseSongNamesTxt = "Files\\LowercaseSongNames.txt"
songNamesTxt = "Files\\SongNames.txt"
songNamesBlanksTxt = "Files\\SongNamesBlanks.txt"

licenseTxt = "Files\\Other Files\\LICENSE.txt"
changelogTxt = "Files\\Other Files\\Changelog.txt"
controlsTxt = "Files\\Other Files\\Controls.txt"

#// Functions //#
def playerAuthorisation():
    #// Player Authorisation //#
    global playerName
    while True:
        playerName = str(input("Please enter your name: "))
        playerName = playerName.upper()
        with open(doNotInputTxt, "r") as doNotInput:
            if playerName in doNotInput.read():
                print("Invalid input, try again.")
                doNotInput.close()
            else:
                with open(authenticatedPlayersTxt, "r") as authenticatedPlayers:
                    if playerName in authenticatedPlayers.read():
                        print("Access Granted.\n")
                        break
                    else:
                        print("Access Denied.")
                        print("Closing...")
                        time.sleep(3)
                        quit()

def newSong():
    #// New Song //#
    global lineChosen
    lineChosen = random.randint(3,12)

    global songChosen
    songChosen = linecache.getline(songNamesTxt, lineChosen)

    global previousSong
    previousSong = songChosen

def displayArtistAndSongBlanks():
    #// Display Artist And Song //#
    newSong()
    print("\nMake sure to use grammar.")
    print("\nThe artist of the song is:", (linecache.getline(artistsTxt,lineChosen)))
    print(linecache.getline(songNamesBlanksTxt, lineChosen))

def openProgram():
    #// Open Program //#
    global inputControl

    while True:
        print("========== Main Menu ==========")
        print("Play Game      - Play the game.")
        print("Controls       - View controls.")
        print("Leaderboard    - View leaderboard.")
        print("Changelog      - View changelog.")
        print("License        - View license.")
        print("Quit           - Quit the program.\n")
        inputControl = str(input("What would you like to do?\nInput: "))
        inputControl = inputControl.upper()
        if inputControl == "PLAY GAME":
            playGame()
        else:
            if inputControl == "CONTROLS":
                with open(controlsTxt, "r") as controls:
                    controlsData = controls.read()
                    print("\n", controlsData, "\n")
                    controls.close()
            else:
                if inputControl == "LEADERBOARD":
                    with open(leaderboardTxt, "r") as leaderboard:
                        leaderboardData = leaderboard.read()
                        print("\n", leaderboardData, "\n")
                        leaderboard.close()
                else:
                    if inputControl == "CHANGELOG":
                        with open(changelogTxt, "r") as changelog:
                            changelogData = changelog.read()
                            print("\n", changelogData, "\n")
                            changelog.close()
                    else:
                        if inputControl == "LICENSE":
                            with open(licenseTxt, "r") as License:
                                licenseData = License.read()
                                print("\n", licenseData, "\n")
                                License.close()
                        else:
                            if inputControl == "QUIT":  
                                print("Closing program...")
                                time.sleep(3)
                                quit()
                            else:
                                if inputControl == "":
                                    print("No input detected, try again.")
                                else:
                                    if inputControl == " ":
                                        print("No input detected, try again.")
                                    else:
                                        print("That's not an option.\n")
                                    
def endGame():
    global points
    global roundCounter
    print("Game Over...")
    with open(lowercaseSongNamesTxt, "r") as lowercaseSongNames:
        lowercaseSongChosen = linecache.getline(lowercaseSongNamesTxt, lineChosen)
        lowercaseSongNames.close()
    print("The correct answer was:", lowercaseSongChosen)
    if roundCounter == 1:
        print("You played 1 round.")
    else:
        print("You played ", roundCounter, " rounds.")
    if points == 1:
        print("You got 1 point.")
    else:
        print("You got",points," points.\n")
        addToLeaderboard()
    points = 0
    roundCounter = 0
    
    while True:
        print("Play again?")
        print("Yes / No")
        optionInput = str(input("Input: "))
        optionInput = optionInput.upper()
        if optionInput == "YES":
            playGame()
        else:
            if optionInput == "NO":
                print("")
                openProgram()
            else:
                print("That's not an option.")

def playGame():
    #// Play Game //#
    global guess1
    global guess2
    global points
    global roundCounter
    global songChosen
    global songNamesTxt

    while True:
        newSong()
        displayArtistAndSongBlanks()
        guess1 = str(input("Guess the song: "))
        guess1 = guess1.upper()
        controlsGuess1()
        noInputGuess1()
        invalidInputGuess1()
        with open(songNamesTxt) as songNames:
            if guess1 in songChosen:
                points += 3
                roundCounter +=1
                print("Correct!")
                songNames.close()
            else:
                guess2 = str(input("Incorrect! Try again: "))
                guess2 = guess2.upper()
                controlsGuess2()
                noInputGuess2()
                invalidInputGuess2()
                if guess2 in songChosen:
                    points += 1
                    roundCounter += 1
                    print("Correct!")
                else:
                    songNames.close()
                    endGame()

def controlsGuess1():
    #// Controls Guess 1 //#
    global guess1
    if guess1 == "STOP":
        endGame()
    if guess1 == "SKIP":
        print("Skipping song...")
        playGame()

def controlsGuess2():
    #// Controls Guess 2 //#
    global guess2
    if guess2 == "STOP":
        endGame()
    if guess2 == "SKIP":
        print("Skipping song...")
        playGame()

def noInputGuess1():
    #// No Input Guess 1 //#
    global guess1
    global noInputMessage
    noInputMessage = "No input detected, try again."
    if guess1 == "":
        print(noInputMessage)
    else:
        if guess1 == " ":
            print(noInputMessage)

def noInputGuess2():
    #// No Input Guess 2 //#
    global guess2
    global noInputMessage
    if guess2 == "":
        print(noInputMessage)
    else:
        if guess2 == " ":
            print(noInputMessage)
        
def invalidInputGuess1():
    #// Invalid Input Guess 1 //#
    global guess1
    global invalidInputMessage
    invalidInputMessage = "Invalid input, try again."
    with open(doNotInputTxt, "r") as doNotInput:
        if guess1 in doNotInput:
            print(invalidInputMessage)
            doNotInput.close()

def invalidInputGuess2():
    #// Invalid Input Guess 2 //#
    global guess2
    global invalidInputMessage
    with open(doNotInputTxt, "r") as doNotInput:
        if guess2 in doNotInput:
            print(invalidInputMessage)
            doNotInput.close()

def addToLeaderboard():
    #// Update Leaderboard //#
    global points
    global playerName
    with open(leaderboardTxt, "a") as leaderboard:
        points = str(points)
        leaderboard.write("\n\nName:   ")
        leaderboard.write(playerName.capitalize())
        leaderboard.write("\n")
        leaderboard.write("Points: ")
        leaderboard.write(points)
        leaderboard.close()
        with open(leaderboardTxt, "r") as leaderboard:
            leaderboardData = leaderboard.read()
            print(leaderboardData, "\n")
            leaderboard.close()

#// Function Calling //
playerAuthorisation()
openProgram()