#CREATED THE MAIN FUNCTION FOR THE CALCULATOR
print("Welcome to Ziad nader simple arithmetic operations calculator !!\n")
def calculator():
    
    #HERE I REQUEST FROM THE USER TO ENTER THE FIRST NUMBER
    def choose_your_first_number():
        
        try:
            x = float(input("Please enter the first number: "))
            
        #HERE I PUT SOME EXCEPTION HANDLING IF THE USER TRIED TO ENTER A CHARACTER OR ANYTHING EXCEPT A NUMBER    
        
        except ValueError:
            print("Error! Please try again and enter a valid number.")
            return choose_your_first_number()
        except OverflowError:
            print("Error! The result is too large to compute.")
            return choose_your_first_number()
        except Exception as e:
            print("A random error occurred! Please try again.")
            return choose_your_first_number()
        return x
    
        
    #HERE I REQUEST FROM THE USER TO ENTER THE SECOND NUMBER
    def choose_your_second_number():
        try:
            y = float(input("Please enter the second number: "))
            
        #HERE I PUT THE SAME EXCEPTION HANDLING I USED ABOVE
        
        except ValueError:
            print("Error! Please try again and enter a valid number.")
            return choose_your_second_number()
        except OverflowError:
            print("Error! The result is too large to compute.")
            return choose_your_second_number()
        except Exception as e:
            print("A random error occurred! Please try again.")
            return choose_your_second_number()
        return y
        
    #HERE I ASKED THE USER TO ENTER HIS CHOSED ARITHMETIC OPERATION
    
    def choose_arithmetic():
        try:
            z = int(input("Please choose the arithmetic operation you want to apply to these two numbers:\n1 - Multiplication\n2 - Addition\n3 - Subtraction\n4 - Division\n"))
    #HERE I MADE IF CONDISTION AND EXCEPTION HANDLING TO MAKE SURE THE USER CHOOSES A NUMBER FROM 1 TO 4        
            if z < 1 or z > 4:
                raise ValueError
        except ValueError:
            print("Error! Please enter a valid number between 1 and 4.")
            return choose_arithmetic()
        except Exception as e:
            print("A random error occurred! Please try again.")
            return choose_arithmetic()
        return z

    x = choose_your_first_number()
    y = choose_your_second_number()
    z = choose_arithmetic()
    
    #IF THE USER CHOOSED MULTIPLICATION
    if z == 1:
        try:
            multiplication = x * y
            print("The result of multiplying", x, "and", y, "is:", multiplication)
        except OverflowError:
            print("Error! The result is too large to compute.")
            return calculator()
        except Exception as e:
            print("A random error occurred! Please try again.")
            
    #IF THE USER CHOOSED ADDITION
    
    elif z == 2:
        try:
            addition = x + y
            print("The result of adding", x, "and", y, "is:", addition)
        except OverflowError:
            print("Error! The result is too large to compute.")
            return calculator()
        except Exception as e:
            print("A random error occurred! Please try again.")
            
    #IF THE USER CHOOSED SUBSTRACTION
    elif z == 3:
        try:
            subtraction = x - y
            subtraction2 = y - x
            print("The result of subtracting", x, "from", y, "is:", subtraction)
            print("The result of subtracting", y, "from", x, "is:", subtraction2)
        except OverflowError:
            print("Error! The result is too large to compute.")
            return calculator()
        except Exception as e:
            print("A random error occurred! Please try again.")
            
    #IF THE USER CHOOSED DIVSION
    elif z == 4:
        try:
            division = x / y
            division2 = y / x
            print("The result of dividing", x, "by", y, "is:", division)
            print("The result of dividing", y, "by", x, "is:", division2)
        except ZeroDivisionError:
            print("Error! You cannot divide by zero. Please try again.")
            return calculator()
        except Exception as e:
            print("A random error occurred! Please try again.")
            
    #A DECISION MAKING WHETER THE USER WANTS TO EXIT OR START FROM ALL OVER AGAIN
    def decision():
        try:
            j = int(input("Choose your next move:\n1 - Exit the Calculator\n2 - Restart the Calculator\n"))
            if j < 1 or j > 2:
                raise ValueError
        except ValueError:
            print("Error! Please enter a valid number.")
            return decision()
        except Exception as e:
            print("A random error occurred! Please try again.")
            return decision()

        if j == 1:
            print ( "Thanks for using my simple calculator!")
        
        
        elif j == 2:
            return calculator()

    return decision()

calculator()