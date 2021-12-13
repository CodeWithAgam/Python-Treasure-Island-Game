# Welcome to Python Mini Treasure Hunt Game
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Print a welcome message
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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')

print("Hi Explorer, and welcome to Treasure Island.")
print("Your mission is to find the Treasure.\n")
   
choice1 = input("You have to start your journey now. Take the Boat by yourself or wait for the Helicopter. Type 'Boat' or 'Helicopter'\n").lower()

if choice1 == "helicopter":

    choice2 = input("Great, you reached the Bahamas! You're on an empty island name Jeff. You need to make a shelter to survive the night. Type 'Find' to find wood or 'Cut' to cut a tree\n").lower()

    if choice2 == "find":

        choice3 = input("Great, you've made a shelter with some extra wood left and also found a cave. Type 'Explore' to explore the cave or 'Weapons' to make weapons\n").lower()

        if choice3 == "weapons":

            choice4 = input("You made an Axe and a Sword. You're now ready to explore the cave and you found the Treasure Chest. Type 'Open' to open it or 'Take' to take it with you\n").lower()

            if choice4 == "C":
                print("Congratulations! You've found the treasure and you've successfully completed the hunt.")      

            else:
                print("Oh no! You were attacked by a tribe while taking the treasure back home. Game Over!")

        else:
            print("Oh no! You entered the cave but there's a bear and you had no weapons to fight. Game Over!")

    else:
        print("oh no! The tree fell over your head. Game Over!")

else:
    print("Oh no! There are sharks in the ocean. Game Over!")