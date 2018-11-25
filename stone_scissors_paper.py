import random

print("----Game----")
print("Stone / Scissors / Paper")
print(" 1) Stone\n", "2) Scissors\n", "3) Paper")
app = random.randint(1, 3)
if app == 1:
    gg = "Stone"
elif app == 2:
    gg = "Scissors"
else:
    gg = "Paper"

try:
    x = int(input("Please make your choise by number: \n"))
    if x == 1:
        print("")
        print("Your choise is Stone")
        print("Opponent choise is ", str(gg))
        print("")
        if app == 1:
            print("Draw!")
        elif app == 2:
            print("You win!")
        else:
            print("You lose!")
        print("")
    elif x == 2:
        print("")
        print("Your choise is Scissors")
        print("Opponent choise is ", str(gg))
        print("")
        if app == 1:
            print("You lose!")
        elif app == 2:
            print("Draw!")
        else:
            print("You win!")
        print("")
    elif x == 3:
        print("")
        print("Your choise is Paper")
        print("Opponent choise is ", str(gg))
        print("")
        if app == 1:
            print("You win!")
        elif app == 2:
            print("You lose!")
        else:
            print("Draw!")
        print("")
    else:
        print("Your input is wrong, please try again with 1 or 2 or 3!")
except:
    print("Error! Write only INT numbers!")