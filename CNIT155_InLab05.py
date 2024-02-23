#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that displays a menu for the user to select. 
# The program has various operations it can perform using the input from the 
# user. Using a loop, it will continue to running the program unless the user 
# chooses the exit option. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main():
    print("                 While Loop Lab")
    print("==============================================================")
    print("1. Print all natural numbers between 1 and N")
    print("2. Display all even natural numbers from 1 to N. Compute their sum and average")
    print("3. Factorial of N")
    print("4. Exit")
    print("==============================================================")

    flag = True
    while flag == True:
        user_input = int(input("Choose one of the following options to perform: "))

        # if the user selects option 1,  it will run the following
        if (user_input == 1):
            
            count = 1 # Sets the count to begin the operation at 1
            N = int(input("Enter a natural number for N: "))
            print(f"Displaying natural numbers between 1 and {N}")

            while count <= N:
                print(count)
                count = count + 1

        # if the user selects option 2,  it will run the following
        elif(user_input == 2):

            count = 1 # Initializes the variable
            sum = 0 # Initializes the variable
            counte = 0 # Initializes the variable
            N = int(input("Enter a natural number for N: "))
            print(f"Displaying even natural numbers from 1 to {N}")
            while count <= N:
                if count % 2== 0:
                     print(count)
                     sum += count
                     counte += 1
                count += 1
            print(f"\nThe sum of even numbers is: {sum}") # Prints the sum of the even numbers
            print(f"The average of even numbers from 1 to {N} is {float(sum/counte)}") # Prints the average of the even numbers

        # if the user selects option 3,  it will run the following
        elif(user_input == 3):
            N = int(input("Enter a natural number for N: "))
            factorialN = math.factorial(N) # calculates the factorial of the user_input
            print(f"\n\nThe factorial of {N} is {factorialN}")
            
        # if the user selects option 4, it will end the program
        elif(user_input == 4):
            flag = False
            print("Goodbye!")
        
        # If the user selects anything other than the options listed, it will ask for a number between 1 and 4
        else:
            print("Invalid Input!\nEnter a number between 1 and 4.")


main()