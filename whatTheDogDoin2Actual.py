# The Game      #99069053 Lennert Bouman

# Ideeen
# Time based gameplay (elke keuze is een uur verder en je hebt maar zo veel uur om je doel te behalen)
# Binnen EN buiten
# Je hebt kater en moet goeie pillen pakken, zoniet maak je foute keuzes (of kun je de beste niet maken) en word je vriendin boos.
# Je vind uit dat DOG investor(of iets anders) van de nieuwe eetzaak (DE PALING) dichtbij huis is.
# Als je nog steeds hoofdpijn hebt rijd je de auto tegen het gebouw aan als je door de drive probeert te gaan en de DOG word boos.

# Presetting variables
endings = 0
bar = "============"
currentLocation = "livingroom"
paling = False
drunk = False
binoculars = False
ladder = False
keys = False
money = False
repeatMain = True
teeth = False
GF = False
ID = False
dogBed = False
TV = False
keys = False
pills = False
sam = False
sam2 = False
activityQuestion = "livingroom"


import time, os , sys


# Printing slow
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.075)

def cancelProgramRequest(variable):
    if variable == "CANCELPROGRAM":
        print("Exiting program.")
        clearScreen(2)
        exit()

def invalidInput():
    print("Invalid input:\n Repeating question.")
    clearScreen(2)
    repeatActivity = True

def repeatGameRequest(): # TO BE CORRECTED
    global repeatActivity
    repeatActivity = False
    time.sleep(2)
    print_slow(f"\n\nWrong ending {ending}.")
    time.sleep(1)
    print_slow(f"\nDo you want to play again for a different ending? \n{bar}\n\
· Yes\n· No\n{bar}\n")
    repeatGameQuestion = input("").upper()
    if repeatGameQuestion == "YES":
        print_slow("The game will now restart from the beginning.")
        enterToContinue()
        time.sleep(0.5)
        sys.stdout.flush()
        os.execv(sys.executable, ['python'] + sys.argv)
    elif repeatGameQuestion == "NO":
        print_slow("The program will now stop execution.\nThank you for playing!")
        enterToContinue()
        exit()
    else:
        invalidInput()

# Function for clearing screen (CLS), parameter is time until execution after initiation.
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def enterToContinue():
    print_slow(f"\n{bar}\nPress Enter ")
    inputEnter = input("")
    cancelProgramRequest(inputEnter)
    clearScreen(1)

# Locations
def relocate(location, pre = "You walk into the "):
    global currentLocation
    print_slow(pre + location + ".")
    clearScreen(2)
    currentLocation = location

def relocateToFunction():
    relocateInput = input("").upper().replace(" ", "").replace("THE", "").replace("!", "").replace("TO", "")
    return relocateInput
relocateInput = relocateToFunction()

def relocateTo():
    global currentLocation
    repeatRelocate = True
    while repeatRelocate:
        repeatRelocate = False
        clearScreen(0.5)
        if currentLocation == "OUTSIDE":
            print_slow(f"You are now {currentLocation}.\nWhere do you want to go?\n{bar}\n")
        else:
            print_slow(f"You are now in the {currentLocation}.\nWhere do you want to go?\n{bar}\n")
        # Living Room
        if currentLocation == "livingroom":
            print_slow(f"· The Kitchen\n· The Hallway\n· The Window\n· The Balcony\n{bar}\n")
            relocateToFunction()
            if relocateInput == "KITCHEN":
                relocate("kitchen")
            elif relocateInput == "HALLWAY":
                relocate("hallway")
            elif relocateInput == "WINDOW":
                relocate("window", "You walk to the ")
            elif relocateInput == "BALCONY":
                relocate("balcony", "You walk onto the ")
            else:
                invalidInput()
        # Kitchen
        elif currentLocation == "kitchen":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateInput == "LIVINGROOM" or relocateInput == "LIVING" or relocateInput == "ROOM":
                relocate("living room")
            else:
                invalidInput()
        # Window
        elif currentLocation == "window":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateInput == "LIVINGROOM" or relocateInput == "LIVING" or relocateInput == "ROOM":
                relocate("living room")
            else: invalidInput()
        # Balcony
        elif currentLocation == "balcony":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateInput == "LIVINGROOM" or relocateInput == "LIVING" or relocateInput == "ROOM":
                relocate("living room")
            else:
                invalidInput()
        # Hallway
        elif currentLocation == "hallway":
            if ladder == True:
                print_slow(f"· The Living Room\n· The Bathroom\n· The Bedroom\n· The Attic\n· Outside\n{bar}\n")
            elif ladder == False:
                print_slow(f"· The Living Room\n· The Bathroom\n· The Bedroom\n· Outside\n{bar}\n")
            relocateToFunction()
            if relocateInput == "LIVINGROOM" or relocateInput == "LIVING" or relocateInput == "ROOM":
                relocate("living room")
            elif relocateInput == "BATHROOM":
                relocate("bathroom")
            elif relocateInput == "BEDROOM":
                relocate("bedroom")
            elif relocateInput == "ATTIC":
                relocate("attic", "You climb up the ladder into the ")
            elif relocateInput == "OUTSIDE":
                if keys == True:
                    relocate("outside", "You walk ")
                elif keys == False:
                    print_slow("You don't have the keys to open the door with you.\n")
                    print_slower('"I gotta go find those keys.."')
            else:
                invalidInput()
        # Bathroom
        elif currentLocation == "bathroom":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateInput == "HALLWAY":
                relocate("hallway")
            else:
                invalidInput()
        # Bedroom
        elif currentLocation == "bedroom":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateInput == "HALLWAY":
                relocate("hallway")
            else:
                invalidInput()
        # Attic
        elif currentLocation == "attic":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateInput == "HALLWAY":
                relocate("hallway")
            else:
                invalidInput()
        # Outside
        elif currentLocation == "outside":
            print_slow(f"· Inside\n· The Clothes Store\n· The Square\n· Snackbar The Paling\n{bar}\n")
            relocateToFunction()
            if relocateInput == "INSIDE":
                relocate("hallway")
            elif relocateInput == "CLOTHESSRE" or relocateInput == "CLOTHES" or relocateInput == 'SRE':
                relocate("clothesstore")
            elif relocateInput == "SQUARE":
                relocate("square", "You walk to the ")
            elif relocateInput == "SNACKBAR" or relocateInput == "PALING" or relocateInput == "SNACKBARPALING":
                relocate("Paling", "You walk into snackbar the ")
            else:
                invalidInput()
        # Clothes Store
        elif currentLocation == "clothesstore":
            print_slow(f"· Back Home\n{bar}\n")
            relocateToFunction()
            if relocateInput == "BACK" or relocateInput == "HOME" or relocateInput == "BACKHOME":
                relocate("outside", "You walk ")
            else:
                invalidInput()
        # Square
        elif currentLocation == "square":
            print_slow(f"· Back Home\n{bar}\n")
            relocateToFunction()
            if relocateInput == "BACK" or relocateInput == "HOME" or relocateInput == "BACKHOME":
                relocate("outside", "You walk ")
            else:
                invalidInput()
        # Snackbar the Paling
        elif currentLocation == "Paling":
            print_slow(f"· Back Home\n·The Managers Office\n{bar}\n")
            relocateToFunction()
            if relocateInput == "BACK" or relocateInput == "HOME" or relocateInput == "BACKHOME":
                relocate("outside", "You walk ")
            elif relocateInput == "MANAGER" or relocateInput == "OFFICE" or relocateInput == "MANAGERSOFFICE":
                relocate("office")
            else:
                invalidInput()

# Activities per location
def activityFunction():
    global activityQuestion
    activityQuestion = input("").upper().replace(" ", "")

def activity():
    global repeatActivity
    global dogBed
    global TV
    global keys
    global pills
    global ladder
    global teeth
    global GF
    global ID
    global money
    global repeatMain
    global drunk
    global paling
    global sam
    global sam2
    picture = False
    repeatActivity = True
    while repeatActivity:
        repeatActivity = False
        clearScreen(0.5)
        if currentLocation == "OUTSIDE":
            print_slow(f"You are now {currentLocation}.\n{bar}\n")
        else:
            print_slow(f"You are now in the {currentLocation}.\n{bar}\n")
        # Living Room
        if currentLocation == "livingroom":
            print_slow(f"· Dog Bed\n· Watch TV\n· Keys\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "DOG" or activityQuestion == "BED" or activityQuestion == "DOGBED":
                if dogBed == False:
                    print_slow("You look at the empty dog bed, you can't help but think about it..\n")
                    time.sleep(1)
                    print_slower('"What is the dog doing..?"')
                    dogBed = True
                elif dogBed == True:
                    print_slow("You look at the empty dog bed again..\n")
                    time.sleep(1)
                    print_slower('"Still no sign of the dog.."')
                enterToContinue()
            elif activityQuestion == "WATCH" or activityQuestion == "TV" or activityQuestion == "WATCHTV":
                if TV == False:
                    print_slow("You turn on the TV and take a look at what's to see.\n\
The only thing there is to see which interests you is a short ad for the recently opened snackbar near your home: Snackbar the Paling.\n")
                    print_slower('"Hm, I should check that place out some time soon."\n')
                    time.sleep(1)
                    print_slow("You turn off the TV.")
                    TV = True
                elif TV == True:
                    print_slow("You turn on the TV again but there is nothing interesting to look at.\n")
                    time.sleep(1)
                    print_slow("You turn off the TV.")
                enterToContinue()
            elif activityQuestion == "KEYS":
                if keys == False:
                    print_slow("\nYou pick up your house keys from the table.")
                    keys = True
                elif keys == True:
                    print_slow("You want to pick up your keys from the table but you realize you already picked them up earlier.\n")
                    print_slower('"Sigh.. I can be so dumb sometimes"')
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Kitchen
        elif currentLocation == "kitchen":
            print_slow(f"· Pain Killers\n· Beer\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "PAIN" or activityQuestion == "KILLERS" or activityQuestion== "PAINKILLERS":
                if pills == False:
                    print_slow("You take a few pain killers that take effect almost immediately.\n")
                    time.sleep(1)
                    print_slower('"Ah much better.."')
                    pills = True
                elif pills == True:
                    print_slow("\nYou look at the empty pot of pain killers.\n")
                    time.sleep(1)
                    print_slower('''"Looks like we're out of painkillers, I should restock sometime soon."''')
                enterToContinue()
            elif activityQuestion == "BEER":
                if drunk == False:
                    print_slow(f"\nYou look in the freezer and see that there is still a bottle of Paling left.\n\
(Your favorite beer)\n\
Will you drink it?\n· Yes\n· No\n{bar}\n")
                    beerQuestion = input("").upper()
                    if beerQuestion == "YES":
                        print_slow("\nYou drink the Paling to every last drop in one go.")
                        drunk = True
                    elif beerQuestion == "NO":
                        print_slow("\nYou decide not to drink the Paling right now and put it back into the freezer.")
                    enterToContinue()
                elif drunk == True:
                    print_slow("\nYou look in the freezer and can't find anything.\nThat Paling was the last thing you had left in the freezer.")
                    enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Window
        elif currentLocation == "window":
            if binoculars == False:
                print_slow(f"· Move\n{bar}\n")
            elif binoculars == True:
                print_slow(f". Binoculars\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "BINOCULARS":
                print_slow("You look out of the window with your binoculars and for a moment think you saw a dog like figure far away from you\n")
                print_slower('"That')
                print_slower("'")
                print_slower('s close to Snackbar the Paling.."')
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Balcony
        elif currentLocation == "balcony":
            global ending
            if drunk == True:
                print_slow("Becaus of the Paling you drank you feel kind of dizzy and lose your balance.\nYou fall to your death...")
                ending = 1
                repeatGameRequest()
            print_slow(f"· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Hallway
        elif currentLocation == "hallway":
            print_slow(f"· Ladder\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LADDER":
                if ladder == False:
                    print_slow("\nYou pull down the ladder to the attic.")
                    ladder = True
                elif ladder == True:
                    print_slow("\nYou already pulled down the ladder.")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Bathroom
        elif currentLocation == "bathroom":
            print_slow(f"· Brush your teeth\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "BRUSH" or activityQuestion == "TEETH" or activityQuestion == "BRUSHYOURTEETH":
                if teeth == True:
                    print_slow("\nYou already brushed your teeth.")
                if teeth == False:
                    print_slow("\nYou brush your teeth.")
                    teeth = True
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Bedroom
        elif currentLocation == "bedroom":
            print_slow(f"· Girlfriend\n· ID\n· Money\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "GIRLFRIEND":
                if GF == False:
                    print_slow("\nYou gently stroke your girlfriends hair and give her a kiss on the forehead.\n")
                    time.sleep(1)
                    print_slower('\n"I')
                    print_slower("'")
                    print_slower('m going out to look for the dog."\n')
                    print_slow("You say softly.\n")
                    time.sleep(1)
                    print_slower('"Okay, come home before evening"\n')
                    print_slow("She said while half asleep.")
                    GF = True
                elif GF == True:
                    print_slow("\nYou gently stroke your girlfriends hair but she gives you a weak push.\n")
                    time.sleep(1)
                    print_slower('\n"Just go already, I')
                    print_slower("'")
                    print_slower('m still trying to sleep."\n')
                    print_slow("She said after being woken up again by you.")
                enterToContinue()
            elif activityQuestion == "MONEY":
                if money == False:
                    print_slow("\nYou silently pick up 20 euros from the night cabinet.")
                    money = True
                elif money == True:
                    print_slow("\nYou already picked up the money from the night cabinet.")
                enterToContinue()
            elif activityQuestion == "ID":
                if ID == False:
                    print_slow("\nYou silently pick up your ID card from the night cabinet.")
                    ID = True
                elif ID == True:
                    print_slow("\nYou already picked up your ID from the night cabinet.")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Attic
        elif currentLocation == "attic":
            print_slow(f"· Search Around\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "SEARCH" or activityQuestion == "SEARCHAROUND":
                if picture == False:
                    print_slow("You look around and find a picture of you and your dog.\n")
                    time.sleep(1)
                    print('\
   ░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░     \n \
   ░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░     \n \
   ░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░     \n \
   ░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░     \n \
   ░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░     \n \
   ░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░     \n \
   ░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░     \n \
   ░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░     \n \
   ░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░     \n \
   ░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░     \n \
   ▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░     \n \
   ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌     \n \
   ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░     \n \
   ░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░     \n \
   ░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░     \n \
   ░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░     \n \
   ░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░     \n \
   ░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░     \n \
   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░     \n \
')
                    time.sleep(1)
                    print_slower('\n"He was still a little pup back then.."\n')
                    print_slow("You think to yourself, remembering the good old days.")
                    picture = True
                elif picture == True:
                    print_slow("You look around but find nothing special anymore.")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Outside
        elif currentLocation == "outside":
            print_slow(f"· Look around you\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("\nYou look around your house for the dog but you can't seem to find him..")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Clothes Store
        elif currentLocation == "clothesstore":
            print_slow(f"· Look around you\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("\nYou look around the store, but the dog is nowhere to be found.")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Square
        elif currentLocation == "square":
            print_slow(f"· Look around you\n· Rodney\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("\nYou look around the square, but the dog is nowhere to be found.")
                enterToContinue()
            elif activityQuestion == "RODNEY":
                print_slow("\nYou walk to Rodney, an old friend of you who seems to have become a beggar because he\n\
kept buying cigarettes he couldn't afford.\n")
                time.sleep(1)
                print_slower('\n"Hey man.. haven')
                print_slower("'")
                print_slower('t seen you in a while.."\n"Do you maybe have some money to lend me so I can buy a chicken burger and some smokes?"\n')
                print_slow("Rodney said..\n")
                time.sleep(1)
                if money == True:
                    print_slow(f"· Yes\n· No\n{bar}\n")
                    money = False
                elif money == False:
                    print_slow(f"· No\n{bar}\n")
                activityFunction()
                if activityQuestion == "YES":
                    print_slow("\nYou give Rodney the 20 euros that you found on your drawer.")
                elif activityQuestion == "NO":
                    print_slow("\nYou refuse to help Rodney and leave him at the square.")
                enterToContinue()
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        # Snackbar the Paling
        elif currentLocation == "Paling":
            if paling == False:
                print_slow('As you get to the entrance of snackbar the Paling you see a classmate from your time at school, Renee.\n\
He is walking in a weird paling-like suit and saying "gast" to customers.\n\
He seems to be playing some sort of mascot.\n')
                paling = True
            if sam == True:
                print_slow(f"· Look around you\n· Mert\n· Sam\n· Lucas\n{bar}\n")
            elif sam == False:
                print_slow(f"· Look around you\n· Mert\n· Sam\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":\
                print_slow("You look around the snackbar but the dog is nowhere to be seen.")
            elif activityQuestion == "MERT":
                print_slow("You walk to Mert, an old friend of you.\n")
                time.sleep(1)
                print_slower('\n"KIP OF KALF!"\n')
                print_slow("Said Mert while tending to the Döner/Kebab.\n")
                time.sleep(1)
                print_slow("You ask if Mert has seen the dog..\n")
                time.sleep(1)
                print_slower('\n"I don')
                print_slower("'")
                print_slower('t know, do you know?"\n')
                print_slow("Mert answered like usual.\n")
                time.sleep(2)
                print_slow("While you cound't get any useful information out of Mert, he DID give you a free Broodje Kebab.")
                enterToContinue()
            elif activityQuestion == "SAM":
                print_slow("\nYou walk to Sam, an old friend of you.\n\
He is currently on break time and eating his sandwiches.\n")
                print_slow(f"· The Dog\n· Renee\n{bar}\n")
                activityFunction()
                if activityQuestion == "DOG":
                    if sam == False:
                        print_slow("You ask Sam if he has seen the dog..\n")
                        print_slower('\n"I heard Lucas talk to the dog a little while ago, maybe he knows."\n')
                        print_slow("Sam answered.")
                        sam = True
                    elif sam == True:
                        print_slow("You ask Sam if he has seen the dog again.\n")
                        print_slower('"I already told you Lucas might know."\n')
                        print_slow("Sam answered.")
                elif activityQuestion == "RENEE":
                    if sam2 == False:
                        print_slow("You ask Sam what Renee is doing in the Paling suit outside the snackbar..\n")
                        time.sleep(1)
                        print_slower('"We hired the guy to be our mascot, the only thing he has to do is walk around and say\n\
"gast" so it should be pretty easy for him.\n')
                        time.sleep(1)
                        print_slower("\nWell that explains..\n")
                        print_slow("You think to yourself.")
                        sam2 = True
                    elif sam2 == True:
                        print_slow("You ask Sam what Renee is doing again.\n")
                        time.sleep(1)
                        print_slower('\n"Look man he is just doing what he is best at, now let me eat."\n')
                        print_slow("Sam answered.")
                enterToContinue()
            elif activityQuestion == "LUCAS":
                print_slow("You walk to Lucas, an old friend of you.\nHe is currently at the back and taking orders for deliveries\
and the drive-through\n")
                time.sleep(0.5)
                print_slow("You ask Lukas if he has seen the dog..\n")
                time.sleep(1)
                print_slower('\n"Yes I have seen the dog, he is upstairs at the moment."\n')
                print_slow("Lucas answered.\n")
                time.sleep(1)
                print_slow("You thank Lukas and go upstairs to the...\n")
                time.sleep(1)
                print_slower('\n"...."\n')
                time.sleep(1)
                print_slower('\n"The Managers office..?"\n')
                enterToContinue()
                print_slow("You open the door and the first thing you see is the dog sitting on the manager's office chair..\n")
                time.sleep(0.5)
                print_slow("You ask the dog...\n")
                time.sleep(2)
                print_slower('\n"So what were you doing?"\n')
                enterToContinue()
                toBeContinued()
                enterToContinue()
                repeatMain = False
            elif activityQuestion == "MOVE":
                relocateTo()
            else:
                invalidInput()
        


# Main program

# Title screen
def startTitleScreen():
    clearScreen(0)
    print(' \
     ___       ___  _______   ___       ________  ________  _____ ______   _______           __________ ________                      \n \
    |\  \     |\  \|\  ____\ |\  \     |\   ____\|\   __  \|\   __\  __  \|\  ____\         |\___   ___|\   __  \                     \n \
    \ \  \    \ \  \ \  \__  \ \  \    \ \  \___|\ \  \ \  \ \  \ \__\ \  \ \  \__          \|___ \  \_\|\  \ \  \                    \n \
     \ \  \  __\ \  \ \  \_\  \ \  \    \ \  \    \ \  \ \  \ \  \/__/\ \  \ \  \_\              \ \  \ \ \  \ \  \                   \n \
      \ \  \_\__\_\  \ \  \____\ \  \____\ \  \____\ \  \_\  \ \  \    \ \  \ \  \_____           \ \  \ \ \  \_\  \  ___  ___  ___   \n \
       \ \____________\ \______ \ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\           \ \__\ \ \_______\ \__\ \__\ \__\  \n \
        \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|            \|__|  \|_______\ |__| |__| |__|  \n \
                                                                                                                                    \n \
                                                                                                                                    \n \
                                                                                                                                ')
    clearScreen(1.5)
    print(' \
     ___       ___  ___  ___  ________  __________    \n \
    |\  \     |\  \|\  \/\  \|\   __  \|\____  ___\   \n \
    \ \  \    \ \  \ \  \_\  \ \  \_\  \|___ \  \_|   \n \
     \ \  \  __\ \  \ \   __  \ \   __  \   \ \  \    \n \
      \ \  \_\__\_\  \ \  \ \  \ \  \ \  \   \ \  \   \n \
       \ \____________\ \__\ \__\ \__\ \__\   \ \__\  \n \
        \|____________|\|__|\|__|\|__|\|__|    \|__|  \n \
                                                    \n \
                                                    \n \
                                                    ')
    clearScreen(1.5)
    print(' \
     __________ ___  ___  _______           ________  ________  ________        \n \
    |\___   ___|\  \/\  \|\  ____\         |\   ___ \|\   __  \|\   ____\       \n \
    \|___ \  \_\ \  \_\  \ \  \__          \ \  \\\ \ \ \  \ \  \ \  \___|       \n \
         \ \  \ \ \   __  \ \  \_\          \ \  \\\ \ \ \  \ \  \ \  \  _____   \n \
          \ \  \ \ \  \ \  \ \  \_____       \ \  \\\_\ \ \  \_\  \ \  \_\   _\  \n \
           \ \__\ \ \__\ \__\ \_______\       \ \_______\ \_______\ \_______\   \n \
            \|__|  \|__|\|__|\|_______|        \|_______|\|_______|\|_______|   \n \
                                                                                \n \
                                                                                \n \
                                                                            ')
    clearScreen(1.5)
    print(' \
     ________  ________  ___  ________     __   \n \
    |\   ___ \|\   __  \|\  \|\   ___  \  /\ \  \n \
    \ \  \\\ \ \ \  \ \  \ \  \ \  \\\ \  \ \ \/  \n \
     \ \  \\\ \ \ \  \ \  \ \  \ \  \\\ \  \ |/   \n \
      \ \  \\\_\ \ \  \_\  \ \  \ \  \\\ \  \     \n \
       \ \_______\ \_______\ \__\ \__\\\ \__\    \n \
        \|_______|\|_______|\|__|\|__| \|__|    \n \
                                                \n \
                                                \n \
                                            ')
    clearScreen(1.5)
    print(' \
     ___       ___  ___  ___  ________  __________                                  ░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░     \n \
    |\  \     |\  \|\  \/\  \|\   __  \|\____  ___\                                 ░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░     \n \
    \ \  \    \ \  \ \  \_\  \ \  \_\  \|___ \  \_|                                 ░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░     \n \
     \ \  \  __\ \  \ \   __  \ \   __  \   \ \  \                                  ░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░     \n \
      \ \  \_\__\_\  \ \  \ \  \ \  \ \  \   \ \  \                                 ░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░     \n \
       \ \____________\ \__\ \__\ \__\ \__\   \ \__\                                ░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░     \n \
        \|____________|\|__|\|__|\|__|\|__|    \|__|                                ░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░     \n \
                                                                                    ░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░     \n \
                                                                                    ░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░     \n \
     __________ ___  ___  _______           ________  ________  ________            ░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░     \n \
    |\___  ___ |\  \/\  \|\  ____\         |\   ___ \|\   __  \|\   ____\           ▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░     \n \
    \|___ \  \_\ \  \_\  \ \  \__          \ \  \\\ \ \ \  \ \  \ \  \___|           ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌     \n \
         \ \  \ \ \   __  \ \  \_\          \ \  \\\ \ \ \  \ \  \ \  \  _____       ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░     \n \
          \ \  \ \ \  \ \  \ \  \_____       \ \  \\\_\ \ \  \_\  \ \  \_\   _\      ░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░     \n \
           \ \__\ \ \__\ \__\ \_______\       \ \_______\ \_______\ \_______\       ░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░     \n \
            \|__|  \|__|\|__|\|_______|        \|_______|\|_______|\|_______|       ░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░     \n \
                                                                                    ░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░     \n \
                                                                                    ░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░     \n \
                                                /\\\\\\\\\\\\\\\\\\\\                         ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░     \n \
                                               /\\\\\///////\\\\\                        \n \
     ________  ________  ___  ________     __  \///      \//\\\\\                        \n \
    |\   ___ \|\   __  \|\  \|\   ___  \  /\ \            /\\\\\\/                       \n \
    \ \  \\\ \ \ \  \ \  \ \  \ \  \\\ \  \ \ \/          _/\\\\\\//                     \n \
     \ \  \\\ \ \ \  \ \  \ \  \ \  \\\ \  \ |/          /\\\\\\//                       \n \
      \ \  \\\_\ \ \  \_\  \ \  \ \  \\\ \  \           /\\\\\\/                         \n \
       \ \_______\ \_______\ \__\ \__\\\ \__\          /\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\   \n \
        \|_______|\|_______|\|__|\|__| \|__|          \///////////////                   \n \
                                                                                        \n \
                                                                                        \n \
            ┌─┐  ┌┐┌┌─┐┬ ┬  ┌┬┐┌─┐┌─┐  ┌─┐┬┌┐┌┌┬┐┬┌┐┌┌─┐  ┌─┐┌┬┐┬  ┬┌─┐┌┐┌┌┬┐┬ ┬┬─┐┌─┐   \n \
            ├─┤  │││├┤ │││   │││ ││ ┬  ├┤ ││││ │││││││ ┬  ├─┤ ││└┐┌┘├┤ │││ │ │ │├┬┘├┤    \n \
            ┴ ┴  ┘└┘└─┘└┴┘  ─┴┘└─┘└─┘  └  ┴┘└┘─┴┘┴┘└┘└─┘  ┴ ┴─┴┘ └┘ └─┘┘└┘ ┴ └─┘┴└─└─┘   \n \
                                                                                        \n \
                                    Press ENTER to begin!                              \n \
                                            ')

def toBeContinued():
    clearScreen(0)
    print(' \
     __________ ________          ________  _______         \n \
    |\___   ___\\\   __  \        |\   __  \|\  ____\       \n \
    \|___ \  \_\ \  \ \  \       \ \  \_\ /\ \  \__         \n \
         \ \  \ \ \  \ \  \       \ \   __  \ \  \_\        \n \
          \ \  \ \ \  \ \  \       \ \  \_\  \ \  \_____    \n \
           \ \__\ \ \_______\       \ \_______\ \_______\   \n \
            \|__|  \|_______|        \|_______|\|_______|   \n \
                                                            \n \
                                                            \n \
     ________  ________  ________   _________  ___  ________   ___  ___  _______   ________          \n \
    |\   ____\|\   __  \|\   ___  \|\___   ___\\\  \|\   ___  \|\  \|\  \|\  ____\ |\   ___ \        \n \
    \ \  \___|\ \  \ \  \ \  \\\ \  \|___ \  \_\ \  \ \  \\\ \  \ \  \\\\\  \ \  \__  \ \  \_|\ \    \n \
     \ \  \    \ \  \ \  \ \  \\\ \  \   \ \  \ \ \  \ \  \\\ \  \ \  \\\\\  \ \  \_\  \ \  \ \\\ \  \n \
      \ \  \____\ \  \_\  \ \  \\\ \  \   \ \  \ \ \  \ \  \\\ \  \ \  \_\  \ \  \____\ \  \_\\\ \   \n \
       \ \_______\ \_______\ \__\\\ \__\   \ \__\ \ \__\ \__\\\ \__\ \_______\ \______\\\ \_______\  \n \
        \|_______|\|_______|\|__| \|__|    \|__|  \|__|\|__| \|__|\|_______|\|_______|\|_______|    ')

startTitleScreen()
beginEnter = input("").upper()
repeatStart = True
while repeatStart:
    repeatStart = False
    clearScreen(0)
    print_slow("Are you ready to jump in yet another adventure?\n\
    · I'm ready!\n\
    · Options\n\
    · Credits\n\
    · Tester mode\n")
    print_slow("============\n")
    questionstart = input("").upper().replace(" ", "").replace("I'M", "").replace("!", "")

    if questionstart == "READY":
        clearScreen(1)
        print_slow("You slowly open your eyes..\n")
        time.sleep(1)
        print_slow("Tired an confuzed you sit up straight and look around you..\n")
        time.sleep(1)
        print_slow("As you observe the room you realize you just woke up on the couch in your living room.\n")
        time.sleep(1)
        print_slower('"What am I doing here?..."\n')
        print_slow("You think to yourself..\n")
        time.sleep(1.5)
        print_slow("At that exact moment you looked at the empty dog bed and remembered what happened last night.\n")
        time.sleep(1.5)
        print_slower("FLASHBACK\n")
        print_slow("============\n")
        print_slow('You hear your dog come home through their doggy door.\nAs they lay down on the doggy bed you made you ask your dog a question.\n"so what were you doing?"\n')
        print_slow("============\n")
        time.sleep(1.5)
        print_slow("You look around the room and realise that ONCE AGAIN your dog is gone.\n")
        time.sleep(1)
        print_slow("Tired and without energy you try to stand up from the couch\n\
    But as you finally stand up straight you realise that a huge hangover kicked in on you because of the party last night.\n")
        time.sleep(1)
        print_slower("I need to do something about this headache..\n")
        print_slow("You thought to yourself.\n")
        enterToContinue()

        while repeatMain:
            activity()

    elif questionstart == "TEST":
        repeat = True
        while repeat:
            repeat = False
            clearScreen(1)
            print(f"Where do you want to start testing?\nType the exact location as mentioned below.\n{bar}")
            print(f"· Livingroom  · Kitchen\n· Balcony  · WIndow\n· Hallway  · Bathroom\n· Bedroom  · Attic\n· Outside  · Store\n· Square  · Paling\n{bar}")
            print(f"Do you want to make certain things positive?\n{bar}")
            if drunk == True:
                print("· Drunk = True")
            else:
                print("· Drunk  = False")
            if binoculars == True:
                print("· Binoculars = True")
            else:
                print("· Binoculars = False")
            if keys == True:
                print("· Keys = True")
            else:
                print("· Keys = False")
            if money == True:
                print("· Money = True")
            else:
                print("· Money = False")
            if ladder == True:
                print("· Ladder = True")
            else:
                print("· Ladder = False")
            if sam == True:
                print(f"· Sam = True\n{bar}")
            else:
                print(f"· Sam = False\n{bar}")
            testModeStart = input("").upper()
            if testModeStart == "LIVINGROOM":
                relocate("living room")
            elif testModeStart == "KITCHEN":
                relocate("kitchen")
            elif testModeStart == "BALCONY":
                relocate("balcony", "You walk onto the ")
            elif testModeStart == "WINDOW":
                relocate("window", "You walk to the ")
            elif testModeStart == "HALLWAY":
                relocate("hallway")
            elif testModeStart == "BATHROOM":
                relocate("bathroom")
            elif testModeStart == "BEDROOM":
                relocate("bedroom")
            elif testModeStart == "ATTIC":
                relocate("attic", "You climb up the ladder into the ")
            elif testModeStart == "OUTSIDE":
                relocate("outside", "You walk ")
            elif testModeStart == "STORE":
                relocate("clothesstore")
            elif testModeStart == "SQUARE":
                relocate("square")
            elif testModeStart == "PALING":
                relocate("Paling") 
            elif testModeStart == "DRUNK":
                drunk = True
                repeat = True
            elif testModeStart == "BINOCULARS":
                binoculars = True
                repeat = True
            elif testModeStart == "KEYS":
                keys = True
                repeat = True
            elif testModeStart == "MONEY":
                money = True
                repeat = True
            elif testModeStart == "LADDER":
                ladder = True
                repeat = True
            elif testModeStart == "SAM":
                sam = True
                repeat = True
            elif testModeStart == "BACK":
                repeatStart = True
            else:
                print_slow("Invalid input, please repeat.")
                time.sleep(1)
                repeat = True

        while repeatMain:
            activity()

    elif questionstart == "OPTIONS":
        print_slow("Just kidding, there's no options for this game.\n")
        time.sleep(1)
        print(' \n \
    ⢰⣶⠶⢶⣶⣶⡶⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⢶⣶⣶⣶⣶ \n \
    ⠘⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⠿⠄⠄⠄⠈⠉⠄⠄⣹⣶⣿⣿⣿⣿⢿ \n \
    ⠄⠤⣾⣿⣿⣿⣿⣷⣤⡈⠙⠛⣿⣿⣿⣧⣀⠠⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶ \n \
    ⢠⠄⠄⣀⣀⣀⣭⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣤⣿⣿⠉⠉⠉⢉⣉⡉⠉⠉⠙⠛⠛ \n \
    ⢸⣿⡀⠄⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣷⣾⣿ \n \
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠛⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⣿⣿⡿⣿⣿⣴⣿⣿⣿⣿⣄⣠⣴⣿⣷⣭⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n \
    ⠸⠿⣿⣿⣿⠋⣴⡟⠋⠈⠻⠿⠿⠛⠛⠛⠛⠛⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⡁⠈⠉⠄⠄⠄⠄⠄⣤⡄⠄⠄⠄⠄⠄⠈⠄⠈⠻⠿⠛⢿⣿⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣠⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⠄⠉⠉⠁⠄⠄⠄⠄⠐⠒⠒⠄⠄⠄⠄⠉⢸⣿⣿⣿ \n \
    ⢸⣿⣿⣿⢿⣦⣄⣠⣄⠛⠟⠃⣀⣀⡀⠄⠄⣀⣀⣀⣀⣀⣀⡀⢀⣰⣦⣼⣿⣿⡿ \n \
    ⢸⣿⣿⣿⣿⣿⣿⣻⣿⠄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣥⣾⣟⣿⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⠿⠿⠿⠿⠿⠿⠿⠿⠿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n \
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        time.sleep(1.5)
        repeatStart = True

    elif questionstart == "CREDITS":
        print_slow("\nGame made by: Lennert Bouman")
        time.sleep(1)
        print_slow("\nAssisted by: Sam Fortuin, Mert Erciyas,Martijn van Houwelingen, Stijn Ooms and Wilfred Bouman.")
        time.sleep(1)
        print_slow("\nAdditionally featured people: Renee, Rodney and Lucas.")
        time.sleep(1)
        print_slow("\nInspired by: Sam Fortuin")
        time.sleep(1)
        print_slow("\nMade for: This game was made for an assignment in school.")
        time.sleep(1)
        print_slow("\nSequel to: What the Dog doing 1 (Made by Sam Fortuin)")
        time.sleep(1)
        print_slow("\nMIGHT be continued.")
        enterToContinue()
        repeatStart = True

    else:
        print("what?")
        time.sleep(1)
        repeatstart = True