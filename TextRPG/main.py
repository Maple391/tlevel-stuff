
#<Made By James mills & RR>
import cmd, textwrap, sys, os, time, random
import mapsRPG
import dialogue_mod


screen_width = 100

settings_color = "0"
gameOver = False
mage_spells = ["Fireball", "Frost Nova", "Arcane Missile", "Teleport", "Invisibility", "Lightning Bolt", "Ice Shield", "Summon Familiar", "Mana Drain", "Blink"]
priest_spells = ["Heal", "Divine Shield", "Smite", "Holy Nova", "Blessing of Strength", "Resurrection", "Purify", "Divine Wrath", "Guardian Spirit", "Spiritual Renewal"]

#### Player setup ####
class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.location = 'Inn'
        self.status_effects = []
        self.inv = []
        self.hands = [] # There will only be two lots
        self.money_cp = 150
        self.money_sp = 30
        self.money_gp = 7
        self.ac = 10 # Armor class

class weapons(): # the way this works is how may times a dice is rowled
    def __init__(self):
        self.dagger = 1  # Damage: 1d6
        self.pike = 3    # Damage: 3d6
        self.bow = 2     # Damage: 2d6
        self.longsword = 4  # Damage: 4d6
        self.mace = 2    # Damage: 2d6
        self.rapier = 4  # Damage: 4d6
        self.staff = 2   # Damage: 2d6
        self.axe = 3     # Damage: 3d6
        self.hammer = 2  # Damage: 2d6
        self.spear = 2   # Damage: 2d6
    
    def get_damage(self, weapon):
        if weapon.lower() == 'dagger':
            return self.dagger
        elif weapon.lower() == 'pike':
            return self.pike
        elif weapon.lower() == 'bow':
            return self.bow
        elif weapon.lower() == 'longsword':
            return self.longsword
        elif weapon.lower() == 'mace':
            return self.mace
        elif weapon.lower() == 'rapier':
            return self.rapier
        elif weapon.lower() == 'staff':
            return self.staff
        elif weapon.lower() == 'axe':
            return self.axe
        elif weapon.lower() == 'hammer':
            return self.hammer
        elif weapon.lower() == 'spear':
            return self.spear
        else:
            print("error")


weapons_ = weapons()
myPlayer = player()
##### title Scrren ####

def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("settings"):
        settings_menu()
    elif option.lower() == ("quit"):
        sys.exit()
        ### settings ###

    elif option.lower() == ("color"):

            print("")
            print("""    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White""")
            settings_color = str(input("Number?> "))
            os.system(f'color {settings_color}')
    while option.lower() not in ["play", "help", "quit"]: # mean the player cant accsidently quit if wrong imput.
        print("Error enter a valid comand.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("settings"):
            settings_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        ### settings ###

        elif option.lower() == ("color"):
            print("")
            print("""    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White""")
            settings_color = input("Number?> ")
            os.system(f'color {settings_color}')
            title_screen_selection()

def title_screen():
    os.system('cls')

    print("+——————————————————————————+")
    print("| welcome to the Text RPG! |")
    print("+——————————————————————————+")
    print("      #   Play   #           ")
    print("      #   Help   #           ")
    print("      # settings #       ")
    print("      #   Quit   #           ")
    print(" (WIP) - Made by James :).")
    title_screen_selection()

def help_menu():
    os.system('cls')
    print("+——————————————————————————+")
    print("| welcome to the Text RPG! | ")
    print("+——————————————————————————+")
    print("# Use up, down, left, right to move")
    print("# Type your commands to do them")
    print("# Use 'look' to inspect somthing ")
    print("# Good look!")
    print("#Is there is a * befor a diolog option it is a integrel question.")
    title_screen_selection()

def settings_menu():
    os.system('cls')
    print("+——————————————————————————+")
    print("| welcome to the Text RPG! | ")
    print("+——————————————————————————+")
    print("      #   color   #          ")
    print("      # Difficulty #           ")
    title_screen_selection()
    
#### MAP ####

#### DEV DESCRIPTIONS ####
"""
Forest: The village is surrounded by a dense forest. Within the forest, there are various locations denoted by letters:

T: Tower of the Druids
H: Herbalist's Hut
?: Anomaly 
P: Potion Maker's Cottage
C: Clearing with a Sacred Stone Circle
M: Mysterious Cave
Village Center: At the heart of the village, there's a bustling center with important establishments:

Shop: A general store where villagers buy goods and supplies.
Inn: A cozy inn where travelers and adventurers stay.
Mountains: In the distance, there are towering mountains, possibly hiding ancient ruins or treasures waiting to be discovered.
"""

#### MAP VARS ####

ZONENAME = ""
DESCRIPTION = "Description"
EXAMINATION = "examine"
EXPLORED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
explored_place = {"T": False, "H": False, "?": False,
                    "P": False, "C": False, "M": False,
                    "Shop": False, "Inn": False, "Moun": False,
                    }


zone_map = {
    "T": {
        ZONENAME: "Tower of the Druids",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "",
        DOWN: "P",
        LEFT:"",
        RIGHT: "H",
        },
    "H": {
        ZONENAME: "Herbalist's Hut",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "H",
        DOWN: "C",
        LEFT:"T",
        RIGHT: "?",
        },
    "?": {
        ZONENAME: "?",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "",
        DOWN: "M",
        LEFT:"H",
        RIGHT: "",
        },
    "P": {
        ZONENAME: "Potion Maker's Cottage",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T",
        DOWN: "Shop",
        LEFT:"",
        RIGHT: "c",
        },
    "C": {
        ZONENAME: "Clearing with a Sacred Stone Circle",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "",
        DOWN: "",
        LEFT:"P",
        RIGHT: "M",
        },
    "M": {
        ZONENAME: "mysterious_cave",
        DESCRIPTION: "A mesterius cave, It looks empty",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "?",
        DOWN: "",
        LEFT:"C",
        RIGHT: "",
        },

    "Shop": {
        ZONENAME: "shop",
        DESCRIPTION: "A general store where villagers buy goods and supplies.",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "P",
        DOWN: "Moun",
        LEFT:"",
        RIGHT: "Inn",
        },
    "Inn": {
        ZONENAME: "The Drunken Inn (Inn/home)",
        DESCRIPTION: "A quaint, weathered inn nestled amidst ancient oaks, its timeworn facade whispering tales of centuries past",
        EXAMINATION: "The inn is old and warm - it looks safe",
        EXPLORED: False,
        UP: "M",
        DOWN: "",
        LEFT:"Shop",
        RIGHT: "",
        },
    "Moun": {
        ZONENAME: "In the distance, there are towering mountains",
        DESCRIPTION: "Description",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "Inn",
        DOWN: "",
        LEFT:"",
        RIGHT: "",
        },
        
    }
#### Game Interactivity ####
def print_location():
    print("\n" + ("—" * (4+ len(myPlayer.location))))
    print(f"- {zone_map [myPlayer.location] [ZONENAME]} #")
    print(f"- {zone_map [myPlayer.location] [DESCRIPTION]} #")
    print("\n" + ("—" * (4+ len(myPlayer.location))))


def prompt():
    print(f"\n=================================")
    print("What would you like to do")
    action = input("> ")
    acceptable_actions = ["move", "go", "travle", "walk", "quit", "examine", "inspect", "look", "map", "look at map", "speek", "talk", "speek to someone"]
    while action.lower() not in acceptable_actions:
        print("Error Unknown action.\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travle", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "look"]:
        player_examine(action.lower)
    elif action.lower() in ["map", "look at map"]:
        MAP_look()
    elif action in ["talk", "speek to someone", "speek"]:
        dialogue(action)

        
def player_move(myAction):
    dest = input("Were would you like to move to?\n>")
    if dest in ["up", "north"]:
        destination = zone_map[myPlayer.location][UP]
        movement_handeler(destination)
    elif dest in ["left", "west"]:
        destination = zone_map[myPlayer.location][LEFT]
        movement_handeler(destination)
    elif dest in ["east", "right"]:
        destination = zone_map[myPlayer.location][RIGHT]
        


def movement_handeler(destination):
    print(f"\nYou have moved to the {destination}.")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zone_map[myPlayer.location][EXPLORED] == True:
        print("You have explored this location.")
    else:
        if zone_map[myPlayer.location][ZONENAME] == "The Drunken Inn (Inn/home)":
            print("You are in the Inn")
            print("")

        if zone_map[myPlayer.location][ZONENAME] == "shop":
            msg = f"The shop is Empty, There is a counter on one corner. Somthing draws you to it."
            for character in msg:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05) 
            x = """\n
            +——————————+———————————————————————+——————————+
            | +——————+ |                       | +——————+ |
            | |   1  | |                       | |  3   | | 
            | +——————+ |                       | +——————+ |
            | +——————+ |                       | +——————+ |
            | |   2  | |                       | |  4   | |
            | +——————+ |                       | +——————+ |
            +——————————+                       +——————————+
            """
            for character in x:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.007)
            correct_draw =  random.randint(1,4)

            for i in range(2):
                attem = 2
                ans = input(f"you have {attem} attemps left: " )
                if ans == correct_draw:
                    pritn("\nThe draw contains one pease of parchment.")
                print("""
                +——————————————————————+
                |  After 3 days here   |
                |  I have found It.    |
                |  The Anomily, a      |
                |  Obelisk that cont-  |
                |  ains somthing.      |
                |  I beleave seting it |
                |  free may give the   |
                |  answers I am look-  | 
                |  ing for. It requires|
                |   some sort of "Key" |
                |  the whaire abouts   |
                |  I beleave to be in  |
                |  in the tower of dr- |
                |  uids. (T).          |
                |    —John smith       |
                +——————————————————————+
                """)
                input("press enter to continue.")
                x = "You hear somone coming..."
                for character in x:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.02)
                break
            else:
                print("You find nothing.")

            


            
            
        else:
            print("True")

def diologue_style(name_0):
    print("\n")
    print("*" * (len(name_0)))
    print("*   "+name_0+"  *")
    print("*"* (len(name_0)))

def dialogue(action):
    ###############—-—INN—-—###############


    if zone_map[myPlayer.location][ZONENAME] == "The Drunken Inn (Inn/home)":
        dialogue_ans = input("There are a few people in the inn it is quiet. people:\n The bar maid(1)\n The stranger(2)\n The knight(3)\n The inn keep(4)\n The drunk(5)\nPick a number to speek to.> ")
        if dialogue_ans == "1":
            name_0 = "The Bar maid"
            
            print("\n")
            valid_questions = ["*What is this place? (1)", "Is there anything i can do?(2)", "What do you have for sale?(3)"]
            diologue_style(name_0)
            bm_speach = "The bar maid: Hi what can i get startd for you, love?\nIf you've any quearys love don't hesitate to ask?"

            print("\n")
           
            for character in bm_speach:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)


            print("\n\nQuestions to ask:")
            for i in range(3):
                print(valid_questions[i])
            print("\n")
            questions = input("> ")
            if questions == "1":
                dialogue_mod.Barmaid_d1()

            elif questions == "2":
                dialogue_mod.Barmaid_d2(myPlayer.name)
            elif questions == "3":
                dialogue_mod.Barmaid_shop()
    ###############—-—INN—-—###############

    elif zone_map[myPlayer.location][ZONENAME] == "shop":
        print("No one is here.")
         





    else:
        print("True")





def MAP_look():
    print("\n====================================================================\n")
    mapsRPG.Grendail_map()
    print("\n====================================================================\n")







#### GAME ####
def swapequiped():
    print("Current Equips:\n")
    print(f"(1) = {myPlayer.equiped[0]}")
    print(f"(2) = {myPlayer.equiped[1]}")
    item = str(input("which item would you like to swap? Type (1) or (0)> "))
    if item == "1":
        myPlayer.inv.append(myPlayer.equiped[0])
        myPlayer.equiped.remove(myPlayer.equiped[0])
        print(f"{myPlayer.equiped[0]}(x1) added to inventory.")
    elif item == "2":
        myPlayer.inv.append(myPlayer.equiped[1])
        myPlayer.equiped.remove(myPlayer.equiped[1])
        print(f"{myPlayer.equiped[1]}(x1) added to invinventory.")
    item = str(input("what item would you like to equiped?: "))
    if item in myPlayer.inv:
        myPlayer.equiped.append(item)
        myPlayer.inv.remove(item)
    
    print()
    print(myPlayer.inv)
    print(myPlayer.equiped)



def choose_spells(player_job):
    available_spells = mage_spells if player_job.lower() == "mage" else priest_spells
    chosen_spells = []
    print("Choose 3 spells from the following list:")
    for index, spell in enumerate(available_spells, start=1):
        print(f"{index}. {spell}")
    
    while len(chosen_spells) < 3:
        try:
            spell_choice = int(input("Enter the number of the spell you want to choose: "))
            if 1 <= spell_choice <= len(available_spells):
                chosen_spell = available_spells[spell_choice - 1]
                if chosen_spell not in chosen_spells:
                    chosen_spells.append(chosen_spell)
                else:
                    print("You've already chosen that spell. Choose a different one.")
            else:
                print("Invalid choice. Please enter a number between 1 and", len(available_spells))
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("\nYou've chosen the following spells:")
    for spell in chosen_spells:
        print(spell)





def main_game_loop():
    while gameOver is False:
        prompt()

### Name Colecting ####





def setup_game():
    os.system('cls')
    
    q1 = "Hello, Whats your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    q2 = "What is your class?\n"
    q2_added = "(You can choose Fighter, Mage, Priest)\n"
    for character in q2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in q2_added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)            
    player_job = input("> ")
    valid_jobs = ["fighter", "mage", "priest"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(f"You choose {player_job}.\n")
        while player_job.lower() not in valid_jobs:
            player_job = input("> ")
            if player_jobs.lower() in valid_jobs:
                myPlayer.job = player_job
    
    if player_job.lower() in ["mage", "priest"]:
        choose_spells(player_job)
        
    if myPlayer.job == "fighter":
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == "mage":
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job == "priest":
        myPlayer.hp = 65
        myPlayer.mp = 60

    
    
    q3 = f"welcome {player_name} the {player_job}\n"
    for character in q3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speach1 = "\nYOu have travled for months, to uncover the misterys of the Plain.\n"
    speach2 = "I hope you find all the answers you were looking for.\n"
    speach3 = "Just make shoure you dont delve too far. You may never return the same...\n"
    speach4 = "Hehehehe..."
    
    for character in speach1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.031)
    for character in speach2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    for character in speach3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    for character in speach4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
    input("To continue Press enter.")
    os.system('cls')
    msg = ("+——————————————————————————+\n|       -=start=-          |\n+——————————————————————————+")
    for character in msg:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    main_game_loop()


#### Shop ####
def Inn_shop():
    while True:
        ans = input("> ")
        if ans.lower == "mead":
                if myPlayer.money_sp >= 15:
                    print("Health restored")
                    if myPlayer.job == "fighter":
                        myPlayer.hp = 120
                        myPlayer.mp = 20
                    elif myPlayer.job == "mage":
                        myPlayer.hp = 40
                        myPlayer.mp = 120
                    elif myPlayer.job == "priest":
                        myPlayer.hp = 65
                    myPlayer.mp = 60
        else:
            print("Error wrong input") 

#### THE GAME START ####    
title_screen()
