#<Made By James mills>
import cmd, textwrap, sys, os, time, random

class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.location = 'Inn'
        self.status_effects = []
        self.inv = []
        self.money_cp = 150
        self.money_sp = 30
        self.money_gp = 7

myPlayer = player()

enigmaOLD = "Ḛ̷̟̃̾̽́̌͘n̸̥̋̈̓͛͆̾͌̀̚i̷̢͐̑͜t̸̖̬̦̠̱͉͕̘͈̾̽̒̾̈͑̒̋̚͠a̸͉̪̖̭̅͛r̶̰̗͓̮̘̺̼͙̫͆̈͗̏́̇̀̈́̚̕z̶̧̈́͌̋́̊̏͗̂ȧ̴͇̙̻͝p̴̢͎͉̣̝͎̔̋͗h̷̯̠͖̘͌͋̿̃̌̆̽̾͝͝"
obeliskold = "ǵ̷̡̞̥̳̘ò̸̢̥̬̞̲̠ơ̸̬̼͈̼͒͂͆̾͛̄͐̍d̵̨̰̟̬͉̔̑ ̸̧̢̞͎̙̪̖̲̓̉̋͛̎͜͝c̵̘̻̖̜͉̖͈̟͈̩̈́̒̏̾̑̋ǒ̶̰̖͓̮̮̙͐ṃ̶̧̹̘̗̪̱̥͙̎͛̑̅ę̶͕̫̖͗̋̃̃̐͐͋̊͊s̴̨̡̰̜͇̩̗̖̣̣̈́ ̶̧̡̫͈͇̠̬̓̈̀͛̌͗̂̾̌ͅf̶̡͇̦͕̱̹͕̥͚̅̐ͅŗ̷̣͇̖̭̀̒͊̾̿́o̷̫͕̰̳͕̼̠̖͚͗͂̈́̒͊̕͘͝m̵̖̆ ̶͖̖̘̻̹͗͗͒̏̐̎̄́͝t̶̼͇̊͊͂̍̎́h̶͎̤̗͉̺͙̮͉͠͝e̴̫̠̳̬̳̟̥̘̹̿͂̉́̉̏͆͝͠ ̸̨̥̣̥̘̙̜̂̂͑̓͌̍͝D̸̩̳̔̆̐̉͘ö̵͎͕̻̹̪̟͎̤͆ͅt̶͕̮̱͙͎̻̜͌͋̏̿͒́͝͝ȑ̸̨̛̖͔̳̪͎͒͂̏̀̈́̑a̴̤̻̭̅̾k̷̡̢̞͔̣͖͙̦͉͚̃ǐ̷̡̞̞͆̋͗͐ė̵̙̠͔̻͓͚̭̙̠̀͋͘̚͝ͅ"

"""Forest: The village is surrounded by a dense forest. Within the forest, there are various locations denoted by letters:

T: Tower of the Druids
H: Herbalist's Hut
?: Anomaly 
P: Potion Maker's Cottage
C: Clearing with a Sacred Stone Circle
M: Mysterious Cave
Village Center: At the heart of the village, there's a bustling center with important establishments:

Shop: A general store where villagers buy goods and supplies.
Inn: A cozy inn where travelers and adventurers stay.
Mountains: In the distance, there are towering mountains, possibly hiding ancient ruins or treasures waiting to be discovered."""



def Barmaid_d1():
    enigmaOLD = "Ḛ̷̟̃̾̽́̌͘n̸̥̋̈̓͛͆̾͌̀̚i̷̢͐̑͜t̸̖̬̦̠̱͉͕̘͈̾̽̒̾̈͑̒̋̚͠a̸͉̪̖̭̅͛r̶̰̗͓̮̘̺̼͙̫͆̈͗̏́̇̀̈́̚̕z̶̧̈́͌̋́̊̏͗̂ȧ̴͇̙̻͝p̴̢͎͉̣̝͎̔̋͗h̷̯̠͖̘͌͋̿̃̌̆̽̾͝͝"
    obeliskold = "ǵ̷̡̞̥̳̘ò̸̢̥̬̞̲̠ơ̸̬̼͈̼͒͂͆̾͛̄͐̍d̵̨̰̟̬͉̔̑ ̸̧̢̞͎̙̪̖̲̓̉̋͛̎͜͝c̵̘̻̖̜͉̖͈̟͈̩̈́̒̏̾̑̋ǒ̶̰̖͓̮̮̙͐ṃ̶̧̹̘̗̪̱̥͙̎͛̑̅ę̶͕̫̖͗̋̃̃̐͐͋̊͊s̴̨̡̰̜͇̩̗̖̣̣̈́ ̶̧̡̫͈͇̠̬̓̈̀͛̌͗̂̾̌ͅf̶̡͇̦͕̱̹͕̥͚̅̐ͅŗ̷̣͇̖̭̀̒͊̾̿́o̷̫͕̰̳͕̼̠̖͚͗͂̈́̒͊̕͘͝m̵̖̆ ̶͖̖̘̻̹͗͗͒̏̐̎̄́͝t̶̼͇̊͊͂̍̎́h̶͎̤̗͉̺͙̮͉͠͝e̴̫̠̳̬̳̟̥̘̹̿͂̉́̉̏͆͝͠ ̸̨̥̣̥̘̙̜̂̂͑̓͌̍͝D̸̩̳̔̆̐̉͘ö̵͎͕̻̹̪̟͎̤͆ͅt̶͕̮̱͙͎̻̜͌͋̏̿͒́͝͝ȑ̸̨̛̖͔̳̪͎͒͂̏̀̈́̑a̴̤̻̭̅̾k̷̡̢̞͔̣͖͙̦͉͚̃ǐ̷̡̞̞͆̋͗͐ė̵̙̠͔̻͓͚̭̙̠̀͋͘̚͝ͅ"


    msg = " The bar maid: This place?...\n"
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    
    time.sleep(2)
    msg = "This place is called grendail. Also known as the Strange forest few people live in the forest, dew to the 'Enigma'."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("\nMe: *Whats the enigma? (1)")
    while True:
        ans = input("> ")
        if ans == "1":
            break
        else:
            print("Error wrong input") 
    msg = f"The bar maid: The 'Enigma' or {enigmaOLD} in old tonge is a Misterius obelisk in the forist, Relics state or {obeliskold}\nor 'No good comes from the Dotrakie' Dotrakie Meaning Old Obelisk." 
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)   


def Barmaid_d2(name):
    msg = "The bar maid: There isn't much work i am afraid love, however there has been strage Ocurences In the forrest,\nResently A adventure like yourself Came by to unlock the obelisk.\nAnd then..."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)   
    msg = "they came..."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.27) 
    print("\nMe: What? (1)")
    while True:
        ans = input("> ")
        if ans == "1":
            break
        else:
            print("Error wrong input") 
    msg = f"The bar maid: We call them the shadow stalkers. The Obolisk commands them some how.\nHead my warning {name} for it may save you."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04) 
    print("\nMe: This other adventuer, DO you know anything about him? (1)")
    while True:
        ans = input("> ")
        if ans == "1":
            break
        else:
            print("Error wrong input") 
    msg = f"errm, I beleave he left some papers of his findings in The local shop."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07) 

def Barmaid_shop():
    msg = f"Have a look love."
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07) 
    
    print("+———————————————————————————+")
    print("| Welcome to the Inn's shop |")
    print("+——————————+———————+————————+")
    print("|  Items   | Stats |  Cost  |")
    print("+——————————+———————+————————+")
    print("| Mead     |  n/a  |  15sp  |")
    print("| Aile     |  n/a  |   5sp  |")
    print("| dagger   |1d6 Dam|   5gp  |")
    print("+——————————+———————+————————+")
    print("Type the name of the item to\nbuy, or type 'back' to exit.")
    print("\n")

    Inn_shop()
    
        
def Inn_shop():
    while True:
        ans = str(input("> "))
        if ans.lower() == "mead":
                if myPlayer.money_sp >= 15:
                    print("Health & Mana restored.")
                    if myPlayer.job == "fighter":
                        myPlayer.hp = 120
                        myPlayer.mp = 20
                    elif myPlayer.job == "mage":
                        myPlayer.hp = 40
                        myPlayer.mp = 120
                    elif myPlayer.job == "priest":
                        myPlayer.hp = 65
                    myPlayer.mp = 60
                    myPlayer.money_sp -= 15
                    print(f"You now have {myPlayer.money_gp}SP in your purse.")
                else:
                    print("Not enugh coin.")
        elif ans.lower() == "mead":
                if myPlayer.money_sp >= 5:
                    print("+25 Health & +25 Mana restored.")
                    if myPlayer.job == "fighter":
                        myPlayer.hp += 25
                        myPlayer.mp += 25
                    elif myPlayer.job == "mage":
                        myPlayer.hp +=25
                        myPlayer.mp += 25
                    elif myPlayer.job == "priest":
                        myPlayer.hp +=25
                    myPlayer.mp += 25
                    myPlayer.money_sp -= 5
                    print(f"You now have {myPlayer.money_gp}SP in your purse.")            
                else:
                    print("not enugh coin.")
        elif ans.lower() == "dagger":
                if myPlayer.money_gp >= 5:
                    print("Dagger(x1) added to your inventoy.")
                    myPlayer.inv.append("Dagger")
                    myPlayer.money_sg -= 5
                    print(f"You now have {myPlayer.money_gp}GP in your purse.")            
                else:
                    print("not enugh coin.")  
        elif ans.lower == "back":
            print("Good bye!")         
        else:
            print("Error wrong input") 