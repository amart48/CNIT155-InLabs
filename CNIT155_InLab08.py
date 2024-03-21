#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will allow users to insert GPA's. The program  
# will calculate the average GPA of the inputs. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main():
    # Ask the user to input how many students are in the class
    n = int(input("Enter the number of students in the class?: "))

    # Create empty lists for student names and student GPAs
    studentNames = []
    studentGPAs = []

    # Loop to add entered names and GPAs based on the user input
    for i in range(n):
        name = input(f"Input student #{i+1} name: ")
        studentNames.append(name)  # Add student name to the list
        while True:
            gpa = float(input(f"Input student #{i+1} GPA: "))
            if 0 <= gpa <= 4.0:  # Check if GPA is within 0 and 4
                studentGPAs.append(gpa)  # Add GPA to the list
                break
            else:
                # If the user inputs anything outside of 0 and 4
                print("A GPA must be between 0 and 4.0 (both inclusive)!\n")

    # Print student names and GPAs
    print("================= List ==================")
    print("        \tName    \tGPA")
    print("        -------              ---------")
    # Loop to print student names and student GPAs
    for name, gpa in zip(studentNames, studentGPAs):
        print(f"        \t{name}    \t{gpa}")
        
    # Find the sum of entered GPAs
    totalGPA = sum(studentGPAs)

    # Find the average of entered GPAs
    averageGPA = totalGPA / n

    # Find the maximum and minimum values among entered GPAs
    maxGPA = max(studentGPAs)
    minGPA = min(studentGPAs)

    # Print the average, maximum, and minimum of entered GPAs with two decimal places
    print("")
    print("="*45)
    print(f"The average of entered GPAs is {averageGPA:.2f}")
    print(f"The maximum GPA is {maxGPA:.2f}")
    print(f"The minimum GPA is {minGPA:.2f}")
    print("="*45)

# Call the main function
main()