# Sam's Game: What the Dog doin'

#99059050, Sam Fortuin
import time, os, sys

#print slow from sabastion on stackoverflow, good lad
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
   
#clears screen after given time
def clearScreen(sleepTime):
  time.sleep(sleepTime)
  os.system("cls")

def invalidInput():
  print("\ninvalid input, exeting program")
  time.sleep(0.2)
  exit()

def listPrint(roomList, roomCount):
  roomCount = len(roomList)
  for i in range(roomCount):
    time.sleep(0.12)
    print(roomList[i])

def invPrint():
  invCount = len(invList)
  for i in range(invCount):
    time.sleep(0.12)
    print("·"+invList[i])

def itemPickup(item,listNum):
  print_slow("\nYou pick up the ")
  print_slow(item)
  print(".\n")
  invList[listNum] = item

#title screen
print(" \
                                                              _____^_       \n  \
                                                            |    |  \       \n  \
                                                            \   /  ^ |      \n  \
                                                           / \_/   0  \     \n  \
                                                          /            \    \n  \
                                                         /    ____      0   \n  \
                                                        /      /  \___ _/   \n  \
             __                __        __    __                      __                          __                       __      \n  \
           /\ \              /\ \__    /\ \__/\ \                    /\ \                        /\ \          __         /\ \      \n  \
 __  __  __\ \ \___      __  \ \ ,_\   \ \ ,_\ \ \___      __        \_\ \    ___      __        \_\ \    ___ /\_\    ___ \ \/      \n  \
/\ \/\ \/\ |\ \  _ `\  /'__`\ \ \ \/    \ \ \/\ \  _ `\  /'__`\      /'_` \  / __`\  /'_ `\      /'_` \  / __`\/\ \ /' _ `\|/       \n  \
\ \ \_/ \_/| \ \ \ \/\ \L\.\_\ \ \_      \ \ \_\ \ \ \ \/\  __/     /\ \L\ \/\ \L\ \/\ \L\ \    /\ \L\ \/\ \L\ \ \ \/\ \/\ \        \n  \
 \ \___x___/  \ \_\ \_\ \__/.\_|\ \__\    \ \__\| \_\ \_\ \____\    \ \___,_\ \____/\ \____ \   \ \___,_\ \____/\ \_\ \_\ \_\       \n  \
  \/__//__/    \/_/\/_/\/__/\/_/ \/__/     \/__/ \/_/\/_/\/____/     \/__,_ /\/___/  \/___L\ \   \/__,_ /\/___/  \/_/\/_/\/_/       \n  \
                                                                                       /\____/                                      \n  \
                                                                                       \_/__/                                       \n  \
                            ┌─┐  ┌┬┐┌─┐┌─┐  ┌─┐┬┌┐┌┌┬┐┬┌┐┌┌─┐  ┌─┐┌┬┐┬  ┬┌─┐┌┐┌┌┬┐┬ ┬┬─┐┌─┐     \n  \
                            ├─┤   │││ ││ ┬  ├┤ ││││ │││││││ ┬  ├─┤ ││└┐┌┘├┤ │││ │ │ │├┬┘├┤      \n  \
                            ┴ ┴  ─┴┘└─┘└─┘  └  ┴┘└┘─┴┘┴┘└┘└─┘  ┴ ┴─┴┘ └┘ └─┘┘└┘ ┴ └─┘┴└─└─┘     \n  \
")
clearScreen(0.5)

#ask which room player wants to go to
print_slow("You return home after a long night of partying.\n\
As you enter the living room you can't find your dog in it's usual spot.\n\
Where will you look for your dog?\n\
·The Kitchen\n·The Bathroom\n·The Bedroom\n")

#input question is in the print_slow above. cleanup is done in the same line
room = input("").lower().replace("the","").replace(" ","")
#clear screen and little bit of text before next question
clearScreen(0.2)
print_slow("You walk towards the ")
print_slow(room)
clearScreen(0.5)

#lists for the 3 items player needs to pick up
invList = ["item0","item1","item2"]
kitchenList = ["·dog food", "·a knife", "·a spoon"]
bathList = ["·soap", "·a towel", "·some toiletpaper"]
bedList = ["·your pillow", "·your bed sheets", "·your sleeping girlfriend"]

#var placeholders for listPrint
kitchenCount = 0
bathCount = 0
bedCount = 0


def roomsItems(itemNum): 
  #if statement for rooms and items
  if room == "kitchen":
    print_slow("You see some items laying in the kitchen:\n")
    listPrint(kitchenList,kitchenCount)
    print_slow("Which one do you pick up?\n")
    itemKitchen = input("").replace(" ","").replace("the","").replace("a","")
    if itemKitchen == "dogfood":
      itemPickup("dog food",itemNum)
      #removes item from the kitchen
      kitchenList.remove("·dog food")
      print_slow("Do you want to eat the dog food?\n")
      dogFoodInput = input("").lower()
      if dogFoodInput == "y" or dogFoodInput == "yes":
        print_slow("In your drunker stupor you eat all the dog food from the can.\nIt's oddly tasty")
        #sets item slot 0 back to clean because player consumed the dog food
        time.sleep(0.5)
        print_slow("\nDo you keep the can or throw it away?\n")
        canKeep = input("").lower()
        if canKeep == "keep":
          print_slow("You decide to keep the can")
          invList[itemNum] = "empty can"
        elif "throw" in canKeep:
          print_slow("You decide to throw away the can.")
          invList[itemNum] = "item"+str(itemNum)
        else:
          print_slow("You can't decide what to do so you just throw the can away")
          invList[itemNum] = "item"+str(itemNum)
      elif dogFoodInput == "n" or dogFoodInput == "no":
        print_slow("You decide to not eat the dog food.")
      else:
        print_slow("You don't quite know what to do with the can so you just take it with you.")
    elif itemKitchen == "knife":
      itemPickup("knife",itemNum)
      #removes the item from the kitchen
      kitchenList.remove("·a knife")
    elif itemKitchen == "spoon":
      itemPickup("spoon",itemNum)
      #removes the item from the kitchen
      kitchenList.remove("·a spoon")
    else:
      invalidInput()

  elif room == "bathroom":
    print_slow("As you enter the bathroom you see:\n")
    listPrint(bathList,bathCount)
    print_slow("what do you pick up?\n")
    # input seperate because of print_slow
    itemBath = input("")
    itemBath = itemBath.replace(" ","").replace("the","").replace("some","").lower()
    if itemBath == "soap":
      itemPickup("soap",itemNum)
      bathList.remove('·soap')
      #removes item from the bathroom
      del bathList[0]
    elif itemBath == "towel" or itemBath == "atowel":
      itemPickup("towel",itemNum)
      #removes the towel from the bathroom list
      bathList.remove('·a towel')
    elif itemBath == "toiletpaper":
      itemPickup("toilet paper",itemNum)
      #removes the toilet paper from the bathroom list
      bathList.remove('·some toiletpaper')
    else:
      invalidInput()
  
  elif room == "bedroom":
    print_slow("As you enter the bedroom you see:\n")
    listPrint(bedList,bedCount)
    print_slow("What do you pick up?\n")
    #input seperate because of print_slow
    itemBed = input("").lower().replace(" ","").replace("your","")
    if itemBed == "pillow":
      itemPickup("pillow",itemNum)
      #removes item from the bedroom
      bedList.remove("·your pillow")
    elif itemBed == "bedsheets":
      itemPickup("bed sheets",itemNum)
      print_slow('While taking the bedsheets you wake up your girlfriend.\nUnderstandably she is not happy with this.\n"Why are you like this?" she asks.')
      gfReplace = bedList.index("·your sleeping girlfriend")
      bedList[gfReplace] = "·your girlfriend"
      bedList.remove("·your bed sheets")
    elif "girlfriend" in itemBed:
      clearScreen(1)
      if "·your sleeping girlfriend" in bedList:
        print_slow('You try pick up your girlfriend.\nShe wakes up as you clumsily continue your pick up attempt.\n"Not this shit again" she says angrily.\nYou put your girlfriend back down in fear she might break up with you.')
        gfReplace = bedList.index("·your sleeping girlfriend")
        bedList[gfReplace] = "·your girlfriend"
      elif "·your girlfriend" in bedList:
        print_slow('You try to pick up your girlfriend for the second time.\nThis time she is already awake so she sees you coming\n"I')
        #seperation because of I've
        print_slow("'ve had it with you!")
        print_slow('"\nShe gets out of bed and walks out the bedroom.\nShe puts on her jacket and grabs her keys.\nShe slams the door behind her and is never seen again.')
        bedList.remove("·your girlfriend")
      else:
        pass
  else:
    invalidInput()

for i in range(3):
  roomsItems(i)
  clearScreen(2.5)
  if i == 0:
    print_slow("As you walk back towards the living room you get the feeling you're still missing something.")
    clearScreen(1.5)
    print_slow("Where do you want to look for the next item?\n·The Kitchen\n·The Bathroom\n·The Bedroom\n")
    room = input("").lower().replace("the","").replace(" ","") 
  elif i == 1:
    print_slow("When you walk back to the living room once again you feel like you need one more thing.")
    clearScreen(1.5)
    print_slow("Where do you want to look for the final item?\n·The Kitchen\n·The Bathroom\n·The Bedroom\n")
    room = input("").lower().replace("the","").replace(" ","")

#empty handed var so ending text from incorrect order doesn't play
emptyHanded = False
#print statements in case an item slot is empty
if "item0" in invList:invList.remove("item0")
if "item1" in invList:invList.remove("item1")
if "item2" in invList:invList.remove("item2")
if len(invList) > 0:
  print_slow("Now that you have collected some items you feel as though you can start calling your dog down in the living room.")
  clearScreen(1.5)
elif len(invList) == 0:
  print_slow('Empty handed you sit down on the couch and think to yourself: "Eh the dog will be fine. But what are they doing?"')
  emptyHanded = True

#dogBedCorrectOrder vars
dogBedCorrectOrder1 = False
dogBedCorrectOrder2 = False
dogBedCorrectOrder3 = False

#doBedOrder list
#empty lists are seen as false
#if any items in invList dog bed building sequence starts
if invList:
  for i in range(len(invList)):
    if i == 0:
      print_slow("Now that you have collected your items.\nYou start prepairing a dog bed in the hopes that your dog will return.\nWhich item do you put down first?\n")
    elif i >= 1:
      print_slow("Which item do you put down next?\n")
    #inv print prints all items in inv with ·. ergo not using listPrint
    invPrint()
    dogBedOrder = input('').lower()
    #item 1 should be towel
    if (dogBedOrder == "towel" or dogBedOrder == "bed sheets") and i == 0:
      dogBedCorrectOrder1 = True
      invList.remove(dogBedOrder)
    #item 2 should be pillow
    elif dogBedOrder == "pillow" and i == 1:
      dogBedCorrectOrder2 = True
      invList.remove(dogBedOrder)
    elif dogBedOrder == "dog food" and i == 2:
      dogBedCorrectOrder3 = True
      invList.remove(dogBedOrder)
    else:
      invList.remove(dogBedOrder)
    clearScreen(1.5)
else:
  pass

if dogBedCorrectOrder1 == True and dogBedCorrectOrder2 == True and dogBedCorrectOrder3 == True:
  print_slow('You hear your dog come home through their doggy door.\nAs they lay down on the doggy bed you made you ask your dog a question.\n"so what were you doing?"')
elif emptyHanded == False:
  print_slow("You sit down on the couch waiting for your dog to come in but they don't come. ")
  print_slow('"Eh they');print_slow("'ll be fine");print_slow('" you say to yourself als you fall asleep on the couch.')

time.sleep(2)
print("\n\n  ______         __            ______            __  __                     __\n\
 /_  __/___     / /_  ___     / ____/___  ____  / /_/_/___  __  _____  ____/ /\n\
  / / / __ \   / __ \/ _ \   / /   / __ \/ __ \/ __/ / __ \/ / / / _ \/ __  / \n\
 / / / /_/ /  / /_/ /  __/  / /___/ /_/ / / / / /_/ / / / / /_/ /  __/ /_/ /  \n\
/_/  \____/  /_.___/\___/   \____/\____/_/ /_/\__/_/_/ /_/\__,_/\___/\__,_/   \n")
