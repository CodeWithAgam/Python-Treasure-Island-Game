# Welcome to Python Mini Treasure Hunt Game
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Class with a welcome message
def Welcome():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')

    print("Hi Explorer, and welcome to Treasure Island.")
    print("Your mission is to find the Treasure.\n")

# Class with the game
def Main():
    print("You have to start your journey now. Take the Boat by yourself or wait for the Helicopter.")
    
    choice1 = input("Type 'B' for Boat or 'H' for Helicopter: ").lower()

    # Continue the game
    if choice1 == "H":
        print("Great, you reached the Bahamas!")
        print("You're on an empty island name Jeff. You've to make a shelter to survive the night.")

        choice2 = input("\nType 'F' to find wood or 'C' to cut a tree: ").lower()
        
        if choice2 == "F":
            print("Great, you've made a shelter with some extra wood left and also found a cave.")

            choice3 = input("\nType 'E' to explore the cave or 'W' to make weapons: ").lower()

            if choice3 == "W":
                print("You made an Axe and a Sword. You're now ready to explore the cave.")

                choice4 = input("\nYou found the Treasure Chest. Type 'C' to open it.").lower()

                if choice4 == "C":
                    print("\nCongratulations! You've found the treasure and you've successfully completed the hunt.")

            else:
                print("Oh no! You entered the cave but there's a bear and you had no weapons to fight. Game Over!")
        
        else:
            print("oh no! The tree fell over your head. Game Over!")

    # End the game
    else:
        print("Oh no! There are sharks in the ocean. Game Over!")

# Call the classes to activate the game
Welcome()
Main()