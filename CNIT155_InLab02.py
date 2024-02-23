#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: The program will gather input from the user to perform 
# various tasks. These tasks are gathering the number of students in CNIT155
# the price of a textbook, today's temperature, and the average speed of a 
# car for a trip. The program will also print out the data type. 
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main(): #Define the main function

    print("This is InLab02 for CNIT155 by Adrian Martinez")
    students_input = input("Enter the number of students in CNIT155: ") # Gets input from the user for the number of students in CNIT155
    print("The number of students in CNIT155 is", students_input)
    students = int(students_input) # Formats the string input to an integer
    print("The data type of the number of students in CNIT155 is",type(students)) # Prints the data type for the number of students

    print("")

    textbook_input = input("Enter the price of a textbook: ") # Gets input from the user for the price of a textbook
    textbook = float(textbook_input)
    print(f"The price of the textbook is $ {textbook:.2f}") 
    print("The data type of the number of the price of a textbook is",type(textbook)) # Prints the data type for the price of a textboook

    print("")

    temp_input = input("Enter today's temperature in Farenheit (°f): ") # Gets input from the user for todays temperature
    temp = float(temp_input)
    celcius = ((temp - 32) * 5 / 9) # Calculates celcius from the inputed farenheit temperature
    print(f"Today's temperature in Celcius is {celcius:.2f} °C")
    print("The data type of the temperature today is",type(celcius))

    print("")

    car_speed_input = input("Enter the distance travelled by a car in miles: ")
    trip_duration_input = input("Enter the duration of the trip in hours: ")
    car_speed = float(car_speed_input)
    trip_duration = float(trip_duration_input)
    average_speed = car_speed / trip_duration
    print(f"The average speed of the car for the trip is {average_speed:.2f} miles/hour ")
    print("The data type of speed is",type(average_speed))

main()
