#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that displays options for the user to choose 
# from. The program can compute various programs such as multiplication tables, 
# triangle numbers, and display even numbers as well. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main():
    flag = True
    while flag == True:
        print("\n\n*************************************************************")
        print("                 For Loops Lab")
        print("*************************************************************")
        print("\n1. Display and add even number from 1 to N")
        print("\n2. Multiplication table of N")
        print("\n3. Print triangle of numbers")
        print("\n4. Exit")
        print("\n*************************************************************")
        user_input = int(input("Choose one of the following options to perform: "))
            
        if (user_input == 1):   
            N = int(input("Enter a natural number for N: ")) # Asks for the user input
            print("Displaying even natural numbers from 1 to",N)
            i = 1 # Initalizing i variable for loop
            sum_even = 0 # Intializes the sum_even variable to later be assigned
            for i in range(2,N+1,2): # Increments the number for every 2            
                print(i)
                sum_even += i
            print("The sum of even natural numbers from 1 to",N,"is",sum_even)

        elif(user_input == 2):
            N = int(input("Enter a natural number for N: ")) # Asks for the user input
            print("Multiplication table of",N)
            i = 1 # Initalizing i variable for loop
            result = 0
            for i in range(i,11): # Repeats the loop from 1 through N
                result = N * i    
                print(N,"x",i,"=",result)

        elif(user_input == 3):
            row = int(input("Enter a number of rows to print triangle of numbers: ")) # Asks for the user input
            i = 1 # Initalizing i variable for loop
            j = 1 # Initalizing j variable 
            for i in range(1,row+2): # Repeats the loop from 1 through the variable row
                for j in range(1,i):
                    print(j,end="")
                print()

        elif(user_input == 4): # If the user inputs 4, the program ends
            flag = False
            print("Goodbye!")

        else:
            print("\n\nInvalid Option!\nPlease choose an option from 1 to 4.")
main()