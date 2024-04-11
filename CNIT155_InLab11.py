#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will read a text file. From the text file, 
# it will create a new text file. This program will then perform various string 
# manipulation that will be added to the new text file. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main():
    try:
        # Using with statement to open books.txt for reading
        with open('books.txt', 'r') as file:
            inputFile = file.readlines()

        # Using with statement to open books_analysis.txt for writing
        with open('books_analysis.txt', 'w') as outputFile:

            print("Printing the contents of the file...\n")
            print(inputFile)

            # Find the number of books in the file
            numBooks = len(inputFile)
            outputFile.write("====== Analysis Results ======\n\n")
            outputFile.write(f"1. The number of books in the file: {numBooks}\n\n")

            # List iteration to find the books with titles of more than 2 words 
            moreThan2WordTitles = [title.strip() for title in inputFile if len(title.split()) > 2]
            # Writing the results of moreThan2WordTitles in the output file
            outputFile.write("2. Titles of Books which have more than 2 words: \n\n")
            for title in moreThan2WordTitles:
                outputFile.write(f"{title}\n")

            # Change all titles of the books to proper case
            proper_case_titles = [title.strip().title() for title in inputFile]
            outputFile.write("\n3. Organized Book Titles :\n\n")
            for title in proper_case_titles:
                outputFile.write(f"{title}\n")
            
        # Close the files
        file.close()
        outputFile.close()

    # If the file cannot be opened...
    except FileNotFoundError:
        print("The program failed to opeen the file. Make sure of followings:")
        print("\t\tThe file to read is located in the same folder where this program is!")
        print("\t\tThe file's name is spelled correctly!")

main()