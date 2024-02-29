#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will compute the perimeter of a triangle.
# It will prompt the user to choose numbers for a b and c side of the triangle 
# and if the variables can create a triangle then it will print the perimeter
# of the triangle using the users input. It will then ask the user if they want to
# continue with the program. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math

def displayMyInfo():
    print("     ","*"*30)
    print("      *    Adrian Martinez         *")
    print("      *    Mart2164@purdue.edu     *")
    print("      *    CNIT155 Lab 07          *")
    print("     ","*"*30)

a = 0 # Initalizing variable for side a of the triangle
b = 0 # Initalizing variable for side b of the triangle
c = 0 # Initalizing variable for side c of the triangle

def validateTriangle(a,b,c): # Checks if variables a, b and c can form a triangle
    if a + b > c and a + c > b and b + c > a:
       print("\nThis is a valid triangle.")
       return True
    else:
        print("\nInputs can not form a triangle. Please enter different numbers!\n")
        return False 

def computePerimeter(a,b,c):
    perimeter = a + b + c # Calculates the perimeter and stores it in the perimeter variable
    return perimeter

def main():
    flag = True # Sets the flag to true to repeat the main function
    while flag ==True:
        a = float(input("Enter the length of side a of a triangle: ")) # Prompts the user to choose a float for the a variable
        b = float(input("Enter the length of side b of a triangle: ")) # Prompts the user to choose a float for the b variable
        c = float(input("Enter the length of side c of a triangle: ")) # Prompts the user to choose a float for the c variable
        print("\nValidating a triangle...")

        if not validateTriangle(a, b, c): # If the validateTriangle function is True, 
            continue
        
        perimeter = computePerimeter(a, b, c)
        print(f"The perimeter of the triangle: {perimeter:.2f}\n") # Print the perimeter of the triangle with 2 decimals
        
        while True:  
            choice = input("Do you want to compute again? (Y/N): ")
            if choice.lower() == 'y': # If the user selects either lower or upper case Y
                break  # If the user selects y, the break will break the while True: loop
            elif choice.lower() == "n": # If the user selects either lower or upper case N
                print("End of the program.")
                flag = False # Sets the flag to false to not run main function again
                break # If the user selects n, the 'break' will break the while True: loop 
            else:
                print("Invalid input.\nPress Y or N, case insensitive:")

displayMyInfo()
main()

