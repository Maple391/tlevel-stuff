class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.location = 'Inn'
        self.status_effects = []
        self.inv = ["Dagger, Hammer"]
        self.equipped = [""]
        self.money_cp = 150
        self.money_sp = 30
        self.money_gp = 7


myPlayer = player()


def inventory():

    print("You open up your bag and you see...")

    for item in myPlayer.inv:
        print(item)
        
    print(f"\nYou open up your purse and see {myPlayer.money_gp} gold pieces, {myPlayer.money_sp} silver pieces and {myPlayer.money_cp} copper pieces.")

    print(f"\nYou have in equipped items, {myPlayer.equipped}")

    swapInput = int(input("\nWould you like to swap(or add) your equipped items?: "))

    if swapInput == 1:
        print("swap")

    
inventory()

#check coins
#check hands
#input 1 to swap equipted