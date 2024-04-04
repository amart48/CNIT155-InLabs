#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will read a file. From that file it will 
# create a new file with an analysis of the data. This includes the max, min, 
# and average of the data. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================
def main():
    try:
        # Open scores.txt 
        inputFile = open("scores.txt", "r")

        # Open scores_stat.txt 
        outputFile = open("scores_stat.txt", "w")

        # Read scores.txt as a list
        scores = inputFile.readlines()

        # Converting score into floats 
        scores = [float(score) for score in scores[3:] if score.strip().replace('.', '').isdigit()]

        # Print the scores
        print("Printing the contents of the file...\n")
        print(scores)

        # Find maximum, minimum, average and length 
        maxScore = max(scores)
        minScore = min(scores)
        avgScore = sum(scores) / len(scores)
        listLength = len(scores)

        # Write the results in scores_stat.txt
        outputFile.write(f"The number of scores in the list is {listLength}\n")
        outputFile.write(f"The average of scores in the list is {avgScore:.2f}\n")
        outputFile.write(f"The maximum score is {maxScore}\n")
        outputFile.write(f"The minimum score is {minScore}")

        # Close the files
        inputFile.close()
        outputFile.close()

    # If the file could not be opened
    except FileNotFoundError:
        print("The program failed to opeen the file. Make sure of followings:")
        print("\t\tThe file to read is located in the same folder where this program is!")
        print("\t\tThe file's name is spelled correctly!")

main()
