#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will calculate the miles the user has 
# walked within a week. The program will use a user defined function for the 
# conversion of steps to miles and will return a list and will print to the 
# console, the results from the user. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

print("\n")
print("*"*60)
print("*"*10+" "*40+"*"*10 )
print("**********       Steps to Miles Calculator        **********")
print("*"*10+" "*40+"*"*10 )
print("*"*60,"\n")

# User defined function to convert steps to miles
def StepsToMiles(lst):
    return [steps / 2000 for steps in lst]

def main():
    # Initializing the stepsList list
    stepsList = []
    # Loop to read the number of steps for 7 days
    day = 1
    while len(stepsList) < 7:
        try:
            # Reading the user input into steps
            steps = int(input(f"Enter the number of steps for day {day}: "))
            # If the user inputs anything other than a positive integer
            if steps < 0:
                raise ValueError
            else:
                stepsList.append(steps)
                day +=1
        # Handle user inputs if they are not a positive integer
        except ValueError:
            print(f"\nException: Wrong Value Entered.\nPlease enter an integer in a correct format!\n")

    # Call StepsToMiles
    miles_walked = StepsToMiles(stepsList)

    # Display miles walked for each day
    print("\n*** The number of miles you walked this week ***")
    day = 1
    # Loop to print the day and how many miles were walked each day
    for miles in miles_walked:
        print(f"Day {day} : {miles:.2f} miles")
        day +=1

    # Calculate and display average miles walked
    averageMiles = sum(miles_walked) / len(miles_walked)
    print(f"\nThe average of miles walked: {averageMiles:.2f}")

    print("\nEnd of the program.")

main()
    