import random
import string

def main_menu():
    print("Welcome to Ziad Nader Password Generator Program")

    while True:
        try:
            length = int(input("Please enter the length of the password: "))
            break
        except ValueError:
            print("Error: Enter a valid number.")
    
    complexity(length)

def complexity(length):
    try:
        complexity1 = int(input(
            "Please choose how complex you want your password:\n"
            "1 - Simple (Characters only)\n"
            "2 - Moderate (Characters and numbers)\n"
            "3 - Difficult (Special characters, numbers, and characters)\n"
            "Choice: "
        ))
        
        if complexity1 == 1:
            characters = string.ascii_lowercase + string.ascii_uppercase
        elif complexity1 == 2:
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        elif complexity1 == 3:
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        else:
            print("Error: Please choose a valid option (1, 2, or 3).")
            return complexity(length)
        
        print("Your Random Password is:\n", "".join(random.choices(characters, k=length)), "\n")
        
        while True:
            try:
                next_choice = int(input(
                    "Please choose what you want to do next:\n"
                    "1 - Generate another random password of the same type\n"
                    "2 - Return to main menu\n"
                    "3 - Exit\n"
                    "Choice: "
                ))
                
                if next_choice == 1:
                    return complexity(length)
                elif next_choice == 2:
                    return main_menu()
                elif next_choice == 3:
                    print("Thanks for using my random password generator.")
                    return
                else:
                    print("Error: Please choose a valid option (1, 2, or 3).")
            except ValueError:
                print("Error: Please enter a valid number.")
    except ValueError:
        print("Error: Please enter a valid number.")
        return complexity(length)

main_menu()