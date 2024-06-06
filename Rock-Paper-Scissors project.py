import random

print("Welcome to Ziad Nader's simple Rock-Paper-Scissors Game !!\n")

#THIS IS THE MAIN MENU FUNCTION THAT DISPLAYS ON THE USER SCREEN WHEN HE STARTS THE PROGRAM
def main_game():


    #HERE I DISPLAYED THE CHOICES THAT THE USER CAN CHOOSE FROM AND MADE SOME EXCEPTION HANDLING 
    try:
        print("Welcome to the Main Menu !!")
        z = int(input("Please make your choice:\n1- Start game\n2- Read the rules\n3- Close the game\n"))
    except ValueError:
        print("Error !! Please choose a valid input")
        return main_game()
    except Exception as e:
        print("A random error happened. Please try again !!")

        return main_game()

#HERE I MADE THAT EVERY CHOICE THE USER WILL DO WILL LEAD TO A CERTAIN PATH

    if z == 1:
        return another_round()
    elif z == 2:
        return rules()
    elif z == 3:
        return close_game()
    else:
        print("Error !! Please choose a valid input")
        return main_game()

#THE FIRST PATH IF THE USER WANTED TO PLAY A ROUND
def another_round():
    user_score = 0
    computer_score = 0

#HERE THE USER MAKES HIS CHOICE WITH SAME USED EXCEPTION HANDLING

    try:
        x = int(input("Please make your choice:\n1- Rock\n2- Paper\n3- Scissors\n"))
    except ValueError:
        print("Error !! Please choose a valid input")
        return another_round()
    except Exception as e:
        print("A random error happened. Please try again !!")
        return another_round()
    
    

#HERE COEMS THE COMPUTER CHOICE AND COMPARING RESULTS

    if x in [1, 2, 3]:
        number = random.randint(1, 3)
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

        if x == number:
            print(f"That's a Tie !! You and the computer both chose {choices[x]} !!")
        elif (x == 1 and number == 3) or (x == 2 and number == 1) or (x == 3 and number == 2):
            print(f"You won !! You chose {choices[x]} and the computer chose {choices[number]} !!")
            user_score += 1
        else:
            print(f"The computer won !! You chose {choices[x]} and the computer chose {choices[number]} !!")
            computer_score += 1

        print(f"Your score is: {user_score}")
        print(f"Computer score is: {computer_score}")
        return finished_game()
    else:
        print("Error !! Please choose a valid input between 1 and 3.")
        return another_round()
    


#HERE COMES THE SECOND PATH WHEN THE USER CHOOSES 2 IN THE MAIN MENU

def rules():
    print("The rules are simple !!\nWhen you start the game you will have to choose one of three things !!\n1- Rock\n2- Paper\n3- Scissors\n")
    print("The computer will also choose one of these choices randomly !!\nRock beats Scissors, Paper beats Rock, and Scissors beat Paper !!")
    print("So if you choose Rock and the computer chooses Scissors, you will win!!\nBut if the computer chooses Paper, it will win !!")
    print("I hope you understand the rules and have fun playing !!\n")
    
    try:
        p = int(input("Press 1 to return to the main menu: "))
    except ValueError:
        print("Please enter a valid number")
        return rules()
    except Exception as e:
        print("A random error happened. Please try again")
        return rules()

    if p == 1:
        return main_game()
    else:
        print("Error !! Please choose a valid input")
        return rules()
#HERE COMES THE THIRD PATH WHEN THE USER CHOOSES 3 IN THE MAIN MENU

def close_game():
    try:
        last_choice = int(input("Are you sure you want to exit? (choose 1 or 2)\n1- Yes\n2- No\n"))
    except ValueError:
        print("Please enter a valid number")
        return close_game()
    except Exception as e:
        print("A random error happened. Please try again")
        return close_game()

    if last_choice == 1:
        print("Thanks for playing !!")
        return 0
    elif last_choice == 2:
        return main_game()
    else:
        print("Error !! Please choose a valid input between 1 and 2.")
        return close_game()
    
#HERE IS FUNCTION THAT WILL BE DISPLAYED AFTER EACH ROUND

def finished_game():
    try:
        m = int(input("You have finished this round. What do you want to do next?\n1- Return to main menu\n2- Play another round\n3- Close the game\n"))
    except ValueError:
        print("Error !! Please choose a valid input")
        return finished_game()
    except Exception as e:
        print("A random error happened. Please try again !!")
        return finished_game()

    if m == 1:
        return main_game()
    elif m == 2:
        return another_round()
    elif m == 3:
        return close_game()
    else:
        print("Error !! Please choose a valid input between 1 and 3.")
        return finished_game()
    
main_game()











                    

        






