#Dice roller program
#This program will select a number between 1 and 6, then it will print the corresponding picture to it.

#imports the random and time functions
import random,time

#set the global variable of the dice number
Dnumber = 0
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

#picks a number between 1 and 6 and saves it to the global variable
def roll():
    global Dnumber
    print("rolling.....")
    Dnumber = random.randint(1,6)
    

#Takes the dice number and pritns out a picture representing that number
def show_dice(roll):
    if Dnumber == 1:
        print(s1)
    elif Dnumber == 2:
        print(s2)
    elif Dnumber == 3:
        print(s3)
    elif Dnumber== 4:
        print(s4)
    elif Dnumber == 5:
        print(s5)
    elif Dnumber == 6:
        print(s6)


#this function asks the user if they want to roll the dice, it will only procced when they enter "y"
def ask_user():
    x=0
    while x == 0:
        choice=input("Do you want to roll the dice? (Enter y)")
        choice=choice.lower()
        if choice == 'y':
            x = 1
        else:
            x = 0
#this function repeats all of these steps until a 6 is rolled
while Dnumber < 6:        
    ask_user()
    roll()
    time.sleep(1)
    show_dice(roll)
