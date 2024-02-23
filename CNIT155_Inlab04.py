#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that calculates simple interest. A program that 
# calculates the compound interest
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math

def main():
    print("==============Menu=============\n")
    print("       Interest Calculator   ")
    print("===============================")
    print("A. Simple interest calculator")
    print("B. Compound interest calculator")
    print("===============================")

    user_input = input("Choose one of the following options to calculate using the interest: ")

    # If the user chooses option A, the following code will be executed
    if user_input == "A":
        print("You chose option A. Simple interest calculator") # Gathers input from the user
        p = float(input("Enter the principal amount: ")) # Gathers input from the user
        t = float(input("Enter the time period in years: ")) # Gathers input from the user
        r = float(input("Enter the interest rate in a percentage %: "))# Gathers input from the user

        A =  p * (1 + (r * t)/100)

        print(f"The final amount in simple interest is $ {A:.2f}")
    # If the user chooses option B, the following code will be executed
    elif user_input == "B":
        print("You chose option B. Compound Interest Calculator") # Gathers input from the user
        p = float(input("Enter the principal amount: ")) # Gathers input from the user
        t = float(input("Enter the time period in years: ")) # Gathers input from the user
        r = float(input("Enter the interest rate in a percentage %: ")) # Gathers input from the user
        n = float(input("Enter the number of terms per years: ")) # Gathers input from the user

        B = p * (math.pow(1 + (r / (100 * n)),(n * t)))

        print(f"The final amount in compound interest is $ {B:.2f}")
    # If the user chooses an option that is not option A or B, it will prompt an error
    else:
        print("Invalid Input!\nPlease enter your choice either A or B")

    
    



main()