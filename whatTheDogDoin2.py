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
drunk = False
binoculars = False
ladder = False
keys = False
money = False
repeatMain = True
timesDogBed = 0
timesTV = 0
timesKeys = 0
timesPills = 0
timesTeeth = 0
timesGF = 0
timesID = 0
activityQuestion = "livingroom"

import time, os , sys

# Printing slow
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

def cancelProgramRequest(variable):
    if variable == "CANCELPROGRAM":
        print("Exiting program.")
        clearScreen(2)
        exit()

def invalidInput():
    print("Invalid input:\n Repeating question.")
    clearScreen(2)
    repeatActivity = True

def repeatGameRequest():
    print_slow(f"Wrong ending {endings}.\nDo you want to play again for a different ending? \n============")
    repeatGameQuestion = input("")

# Function for clearing screen (CLS), parameter is time until execution after initiation.
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

# Locations
def relocateToKitchen():
    print_slow("You walk into the kitchen.")
    clearScreen(2)
    currentLocation = "kitchen"
def relocateToHallway():
    print_slow("You walk into the hallway.")
    clearScreen(2)
    currentLocation = "hallway"
def relocateToWindow():
    print_slow("You walk to the window.")
    clearScreen(2)
    currentLocation = "window"
def relocateToBathroom():
    print_slow("You walk into the bathroom.")
    clearScreen(2)
    currentLocation = "bathroom"
def relocateToBedroom():
    print_slow("You walk into the bedroom.")
    clearScreen(2)
    currentLocation = "bedroom"
def relocateToLivingRoom():
    print_slow("You walk into the living room.")
    clearScreen(2)
    currentLocation = "livingroom"
def relocateToAttic():
    print_slow("You climb up the ladder into the attic.")
    clearScreen(2)
    currentLocation = "attic"
def relocateToBalcony():
    print_slow("You walk onto the balcony.")
    clearScreen(2)
    currentLocation = "balcony"
def relocateToOutside():
    print_slow("You walk outside.")
    clearScreen(2)
    currentLocation = "outside"
def relocateToClothesStore():
    print_slow("You walk to the clothes store.")
    clearScreen(2)
    currentLocation = "clothesstore"
def relocateToSquare():
    print_slow("You walk to the square.")
    clearScreen(2)
    currentLocation = "square"
def relocateToPaling():
    print_slow("You walk to snackbar the Paling.")
    clearScreen(2)
    currentLocation = "Paling"
def relocateToManager():
    print_slow("You walk to the manager's office.")
    clearScreen(2)
    currentLocation = "office"

def relocateToFunction():
    global relocateTo
    global keys
    relocateTo = input("").upper().replace(" ", "").replace("THE", "").replace("!", "").replace("TO", "")

def relocate():
    global currentLocation
    repeatRelocate = True
    while repeatRelocate:
        repeatRelocate = False
        print_slow(f"You are now {currentLocation}.\nWhere do you want to go?\n")
        # Living Room
        if currentLocation == "livingroom":
            print_slow(f"· The Kitchen\n· The Hallway\n· The Window\n· The Balcony\n{bar}\n")
            relocateToFunction()
            if relocateTo == "KITCHEN":
                relocateToKitchen()
            elif relocateTo == "HALLWAY":
                relocateToHallway()
            elif relocateTo == "WINDOW":
                relocateToWindow()
            elif relocateTo == "BALCONY":
                relocateToBalcony()
            else:
                invalidInput()
        # Kitchen
        elif currentLocation == "kitchen":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateTo == "LIVINGROOM" or relocateTo == "LIVING" or relocateTo == "ROOM":
                relocateToLivingRoom()
            else:
                invalidInput()
        # Window
        elif currentLocation == "window":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateTo == "LIVINGROOM" or relocateTo == "LIVING" or relocateTo == "ROOM":
                relocateToLivingRoom()
            else: invalidInput()
        # Balcony
        elif currentLocation == "balcony":
            print_slow(f"· The Living Room\n{bar}\n")
            relocateToFunction()
            if relocateTo == "LIVINGROOM" or relocateTo == "LIVING" or relocateTo == "ROOM":
                relocateToLivingRoom()
            else:
                invalidInput()
        # Hallway
        elif currentLocation == "hallway":
            if ladder == True:
                print_slow(f"· The Living Room\n· The Bathroom\n· The Bedroom\n· The Attic\n· Outside\n{bar}\n")
            elif ladder == False:
                print_slow(f"· The Living Room\n· The Bathroom\n· The Bedroom\n ·Outside\n{bar}\n")
            relocateToFunction()
            if relocateTo == "LIVINGROOM" or relocateTo == "LIVING" or relocateTo == "ROOM":
                relocateToLivingRoom()
            elif relocateTo == "BATHROOM":
                relocateToBathroom()
            elif relocateTo == "BEDROOM":
                relocateToBedroom()
            elif relocateTo == "ATTIC":
                relocateToAttic()
            elif relocateTo == "OUTSIDE":
                if keys == True:
                    relocateToOutside()
                elif keys == False:
                    print_slow("You don't have the keys to open the door with you.")
                    print_slower('"I gotta go find those keys.."')
            else:
                invalidInput()
        # Bathroom
        elif currentLocation == "bathroom":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateTo == "HALLWAY":
                relocateToHallway()
            else:
                invalidInput()
        # Bedroom
        elif currentLocation == "bedroom":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateTo == "HALLWAY":
                relocateToHallway()
            else:
                invalidInput()
        # Attic
        elif currentLocation == "attic":
            print_slow(f"· The Hallway\n{bar}\n")
            relocateToFunction()
            if relocateTo == "HALLWAY":
                relocateToHallway()
            else:
                invalidInput()
        # Outside
        elif currentLocation == "outside":
            print_slow(f"· Inside\n· The Clothes Store\n· The Square\n· Snackbar The Paling\n{bar}\n")
            relocateToFunction()
            if relocateTo == "INSIDE":
                relocateToHallway()
            elif relocateTo == "CLOTHESSTORE" or relocateTo == "CLOTHES":
                relocateToClothesStore()
            elif relocateTo == "SQUARE":
                relocateToSquare()
            elif relocateTo == "SNACKBAR" or relocateTo == "PALING" or relocateTo == "SNACKBARPALING":
                relocateToPaling()
            else:
                invalidInput()
        # Clothes Store
        elif currentLocation == "clothesstore":
            print_slow(f"· Back Home\n{bar}\n")
            relocateToFunction()
            if relocateTo == "BACK" or relocateTo == "HOME" or relocateTo == "BACKHOME":
                relocateToOutside()
            else:
                invalidInput()
        # Square
        elif currentLocation == "square":
            print_slow(f"· Back Home\n{bar}\n")
            relocateToFunction()
            if relocateTo == "BACK" or relocateTo == "HOME" or relocateTo == "BACKHOME":
                relocateToOutside()
            else:
                invalidInput()
        # Snackbar the Paling
        elif currentLocation == "Paling":
            print_slow(f"· Back Home\n·The Managers Office\n{bar}\n")
            relocateToFunction()
            if relocateTo == "BACK" or relocateTo == "HOME" or relocateTo == "BACKHOME":
                relocateToOutside()
            elif relocateTo == "MANAGER" or relocateTo == "OFFICE" or relocateTo == "MANAGERSOFFICE":
                relocateToManager()
            else:
                invalidInput()
        # Office
        elif currentLocation == "office":
            print_slow(f"· Back to the store\n{bar}\n")
            relocateToFunction()
            if relocateTo == "BACK" or relocateTo == "STORE" or relocateTo == "BACKSTORE":
                relocateToPaling()
            else:
                invalidInput()

# Activities per location
def activityFunction():
    global activityQuestion
    activityQuestion = input("").upper().replace(" ", "")

def activity():
    global timesDogBed
    global timesTV
    global timesKeys
    global timesPills
    global ladder
    global timesTeeth
    global timesGF
    global timesID
    global money
    global repeatMain
    global repeatActivity
    repeatActivity = True
    while repeatActivity:
        repeatActivity = False
        clearScreen(0.5)
        print_slow(f"You are now {currentLocation}.\n")
        # Living Room
        if currentLocation == "livingroom":
            print_slow(f"· Dog Bed\n· Watch TV\n· Keys\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "DOG" or activityQuestion == "BED" or activityQuestion == "DOGBED":
                timesDogBed += 1
                if timesDogBed == 1:
                    print_slow("You look at the empty dog bed, you can't help but think about it..\n")
                    time.sleep(1)
                    print_slower('"What is the dog doing..?"\n')
                elif timesDogBed > 1:
                    print_slow("You look at the empty dog bed again..")
                    time.sleep
                    print_slower('"Still no sign of the dog.."')
            elif activityQuestion == "WATCH" or activityQuestion == "TV" or activityQuestion == "WATCHTV":
                timesTV += 1
                if timesTV == 1:
                    print_slow("You turn on the TV and take a look at what's to see.\n\
The only thing there is to see which interests you is a short ad for the recently opened snackbar near your home: Snackbar the Paling\n")
                    print_slower('"Hm, I should check that place out some time soon."')
                    time.sleep(1)
                    print_slow("You turn off the TV.")
                elif timesTV > 1:
                    print_slow("You turn on the TV again but there is nothing interesting to look at.")
                    time.sleep(1)
                    print_slow("You turn off the TV.")
            elif activityQuestion == "KEYS":
                keys = True
                timesKeys += 1
                if timesKeys == 1:
                    print_slow("You pick up your house keys from the table.")
                elif timesKeys > 1:
                    print_slow("You want to pick up your keys from the table but you realize you already picked them up earlier.")
                    print_slower('"Sigh.. I can be so dumb sometimes"')
        # Kitchen
        elif currentLocation == "kitchen":
            print_slow(f"· Pain Killers\n· Beer\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "PAIN" or activityQuestion == "KILLERS" or "PAINKILLERS":
                timesPills += 1
                if timesPills == 1:
                    print_slow("You take a few pain killers that take effect almost immediately.")
                    time.sleep(1)
                    print_slower("Ah much better..")
                elif timesPills > 1:
                    print_slow("You look at the empty pot of pain killers.")
                    time.sleep(1)
                    print_slower('"Those from earlier were the last ones it seems.."')
            if activityQuestion == "BEER":
                print_slow(f"You look in the freezer and see that there is still a bottle of Paling left.\n\
Do you drink it?\n· Yes\n· No\n{bar}\n")
                beerQuestion = input("").upper()
                if beerQuestion == "YES":
                    print_slow("You drink the Paling to every last drop in one go.")
                    drunk = True
                elif beerQuestion == "NO":
                    print_slow("You decide not to drink the Paling right now and put it back into the freezer.")
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
        # Balcony
        elif currentLocation == "balcony":
            if drunk == True:
                print_slow("Becaus of the Paling you drank you feel kind of dizzy and lose your balance.\nYou fall to your death.")
                repeatMain = False
            print_slow(f"· Move\n{bar}\n")
            activityFunction()
        # Hallway
        elif currentLocation == "hallway":
            print_slow(f"· Ladder\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LADDER":
                if ladder == False:
                    print_slow("You pull down the ladder to the attic.")
                    ladder = True
                elif ladder == True:
                    print_slow("You already pulled down the ladder.")
        # Bathroom
        elif currentLocation == "bathroom":
            print_slow(f"· Brush your teeth\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "BRUSH" or activityQuestion == "TEETH" or activityQuestion == "BRUSHYOURTEETH":
                timesTeeth += 1
                if timesTeeth == 1:
                    print_slow("You brush your teeth.")
                elif timesTeeth > 1:
                    print_slow("You already brushed your teeth.")
        # Bedroom
        elif currentLocation == "bedroom":
            print_slow(f"· Girlfriend\n· ID\n· Money\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "GIRLFRIEND":
                timesGF += 1
                if timesGF == 1:
                    print_slow("You gently stroke your girlfriends hair and give her a kiss on the forehead.\n")
                    time.sleep(1)
                    print_slower('\n"I')
                    print_slower("'")
                    print_slower('m going out to look for the dog."\n')
                    print("You say softly.\n")
                    time.sleep(1)
                    print_slower('\n"Okay, come home before evening"\n')
                    print_slow("She said while half asleep.\n")
                elif timesGF > 1:
                    print_slow("You gently stroke your girlfriends hair but she gives you a weak push.\n")
                    time.sleep(1)
                    print_slower('\n"Just go already, I')
                    print_slower("'")
                    print_slower('m still trying to sleep."\n')
                    print_slow("She said after being woken up again by you.\n")
            elif activityQuestion == "MONEY":
                if money == False:
                    print_slow("You silently pick up 20 euros from the night cabinet.")
                elif money == True:
                    print_slow("You already picked up the money from the night cabinet.")
            elif activityQuestion == "ID":
                if timesID == False:
                    print_slow("You silently pick up your ID card from the night cabinet.")
                    ID = True
                elif timesID == True:
                    print_slow("You already picked up your ID from the night cabinet.")
        # Attic
        elif currentLocation == "attic":
            print_slow(f"· Search Around\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "SEARCH" or activityQuestion == "SEARCHAROUND":
                if picture == False:
                    print_slow("You look around and find a picture of you and your dog.\n")
                    print_slower("\nHe was still a little pup back then..\n")
                    print_slow("You think to yourself, remembering the good old days.\n")
                    picture = True
                elif picture == True:
                    print_slow("You look around but find nothing special anymore.")
        # Outside
        elif currentLocation == "outside":
            print_slow(f"· Look around you\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("You look around your house for the dog but you can't seem to find him..")
        # Clothes Store
        elif currentLocation == "clothesstore":
            print_slow(f"· Look around you\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("You look around the store, but the dog is nowhere to be found.")
        # Square
        elif currentLocation == "square":
            print_slow(f"· Look around you\n· Rodney\n· Move\n{bar}\n")
            activityFunction()
            if activityQuestion == "LOOK" or activityQuestion == "LOOKAROUND" or activityQuestion == "LOOKAROUNDYOU":
                print_slow("You look around the square, but the dog is nowhere to be found.")
            elif activityQuestion == "RODNEY":
                print_slow("You walk to Rodney, an old friend of you who seems to have become a beggar because he\n\
kept buying cigarettes he couldn't afford.\n")
                time.sleep(1)
                print_slower('\n"Hey man.. haven')
                print_slower("'")
                print_slower('t seen you in a while.."\n"Do you maybe have some money to lend me so I can buy a chicken burger and some smokes?"\n')
                print_slow("Rodney said..")
                time.sleep(1)
                if money == True:
                    print_slow(f"· Yes\n· No\n{bar}\n")
                elif money == False:
                    print_slow(f"· No\n{bar}\n")
                activityFunction()
                if activityQuestion == "YES":
                    print_slow("You give Rodney the 20 euros that you found on your drawer.")
                elif activityQuestion == "NO":
                    print_slow("You refuse to help Rodney and leave him at the square.")
        # Snackbar the Paling
        elif currentLocation == "Paling":
            if paling == False:
                firstTimeText()
                paling = True
            if sam == True:
                print_slow(f"· Look around you\n· Mert\n· Sam\n· Lukas\n{bar}\n")
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
                print_slower("I don't know, do you know?")
                print_slow("Mert answered like usual.")
                time.sleep(2)
                print_slow("While you cound't get any useful information out of Mert, he DID give you a free Broodje Kebab.")
            elif activityQuestion == "SAM":
                print_slow("You walk to Sam, an old friend of you.\n\
He is currently on break time and eating his sandwiches.\n")
                print_slow(f"· The Dog\n· Renee\n{bar}\n")
                activityFunction()
                if activityQuestion == "DOG":
                    if sam == False:
                        print_slow("You ask Sam if he has seen the dog..\n")
                        print_slower('\n"I heard Lukas talk to the dog a little while ago, maybe he knows."\n')
                        print_slow("Sam answered.")
                        sam = True
                    elif sam == True:
                        print_slow("You ask Sam if he has seen the dog again.\n")
                        print_slower('"I already told you Lukas might know."\n')
                        print_slow("Sam answered.")
                elif activityQuestion == "RENEE":
                    if sam2 == False:
                        print_slow("You ask Sam what Renee is doing in the Paling suit outside the snackbar..")
                        time.sleep(1)
                        print_slower('"We hired the guy to be our mascot, the only thing he has to do is walk around and say\n\
"gast" so it should be pretty easy for him.')
                        time.sleep(1)
                        print_slower("Well that explains..\n")
                        print_slow("You think to yourself.")
                        sam2 = True
                    elif sam2 == True:
                        print_slow("You ask Sam what Renee is doing again.\n")
                        time.sleep(1)
                        print_slower('\n"Look man he is just doing what he is best at, now let me eat."\n')
                        print_slow("Sam answered.")
            elif activityQuestion == "LUKAS":
                print_slow("You walk to Lukas, an old friend of you.\nHe is currently at the back and taking orders for deliveries\
and the drive-through\n")
                time.sleep(0.5)
                print_slow("You ask Lukas if he has seen the dog..\n")
                time.sleep(1)
                print_slower('\n"Yes I have seen the dog, he is upstairs at the moment."\n')
                print_slow("Lukas answered.\n")
                time.sleep(1)
                print_slow("You thank Lukas and go upstairs to the...\n")
                time.sleep(1)
                print_slower('\n"...."\n')
                time.sleep(1)
                print_slower('\n"The Managers office..?"\n')
                time.sleep(1)
                print_slow("You open the door and the first thing you see is the dog sitting on the manager's office chair..\n")
                time.sleep(0.5)
                print_slow("You ask the dog...\n")
                time.sleep(2)
                print_slower('\n"So what were you doing?"\n')
                print_slower(f"\n{bar}")
                endEnter = input("Press ENTER")
                repeatMain = False
        if activityQuestion == "MOVE":
            relocate()
        else:
            invalidInput()
        

                
def firstTimeText():
    if currentLocation == "at snackbar the Paling":
        print_slow('As you get to the entrance of snackbar the Paling you see a classmate from your time at school, Renee.\n\
He is walking in a weird paling-like suit and saying "gast" to customers.\n\
He seems to be playing some sort of mascot.\n')

# Main program

# Title screen
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
beginEnter = input("").upper()
clearScreen(0)
print_slow("Are you ready to jump in yet another adventure?\n\
· I'm ready!\n\
· Options (WIP)\n\
· Credits (WIP)\n")
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
    beginEnter = input("")

    while repeatMain:
        activity()
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