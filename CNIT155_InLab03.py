#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will use the input from a user to perform
# multiople calculations. The program will calculate the volume of a truncated 
# cone. The program will calculate the lateral area of the truncated cone.
# The program will calculate the surface area of a truncated cone. Finally, the 
# the program will print the calculated outputs of the program.  
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main():

    print("         Properties of a Truncated Cone")
    print("         -------------------------------")

    radius1_cone = float(input("Enter the radius 1 (r1) of a cone: ")) #Gathers input fromt he user for radius 1
    height_cone = float(input("Enter the height of a cone: ")) #Gathers input for the height of the cone from the user
    height_slant_cone = float(input("Enter the slant height of a cone: ")) #Gathers  slant height of a cone from the user 
    radius2_cone = float(input("Enter the radius 2 (r2) of a cone: ")) #Gathers input from the user for radius 2 is formatted as a float

    cone_volume = (1/3) * math.pi * height_cone * (pow(radius1_cone, 2) + pow(radius2_cone, 2) + (radius1_cone * radius2_cone)) # Performs the function for the volume of the cone with the inputs from the user

    cone_lateral_area = height_slant_cone * math.pi * (radius1_cone + radius2_cone) # Performs the function for the lateral area of the cone with the inputs from the user

    Total_Surface_area  = cone_lateral_area + math.pi * (pow(radius1_cone, 2) + pow(radius2_cone, 2)) # Performs the function for the total surface area of the cone with the inputs from the user

    print("")
    print("----------------------------------------------")
    print("Calculating..")
    print("")
    
    print(f"The volume of the truncated cone is: {cone_volume:.2f}") # Prints the calcualted volume of the truncated cone
    print(f"The lateral area of the truncated cone is: {cone_lateral_area:.2f}") # Prints the calcualted lateral area of the truncated cone
    print(f"The surface area of the truncated cone is: {Total_Surface_area:.2f}") # Prints the calcualted surface area of the truncated cone


main()