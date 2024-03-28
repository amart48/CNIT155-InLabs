#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will gather user inputs into a list. From
# that list, it will calculate USD to Yuan. It will then print the conversion and
# calculate the average for the inputted prices. It will then show prices under 70
# USD. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def UsdtoYuan(lst):
    exchangeRate = 7.21
    yuanList = []
    # Loop to append the Yuan to yuanList
    for i in range (len(lst)):
        yuanList.append(float(lst[i] * exchangeRate))
    return yuanList

def PrintInfo(lst1, lst2):
    print("\tUSD($)\t\tYuan(¥)")
    print("#"*50)
    # Loop to print the info for USD and Yuan
    for i in range(len(lst1)):
        print(f"\t{lst1[i]:.2f}\t\t{lst2[i]:.2f}")

# Calculate the average of list
def Average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

def FindPrice(lst1, lst2):
    print("#############Price(s) under $70 is (are)#############")
    print("\tUSD($)\t\tYuan(¥)")
    print("\t-------\t\t--------")
    # Loop to find prices that are 70 USD or under
    for i in range(len(lst1)):
        if lst1[i] < 70:
            print(f"\t{lst1[i]:.2f}\t\t{lst2[i]:.2f}")
            
def main():
    USD = []
    flag = True
    # While loop to get user inputs 
    while flag == True:
        priceInput = input("Enter a price in USD. Use NN or nn to stop data entry: ")
        # If user inputs NN or nn, the loop will break
        if priceInput.lower() == "nn":
            break
        # If the user inputs anything else, it will be added to the USD list
        else:
            USD.append(float(priceInput))

    # Print the number of prices entered
    print(f"Number of prices entered: {len(USD)}\n")
        
    # Call UsdtoYuan function
    Yuan = UsdtoYuan(USD)
    
    # Call PrintInfo function
    PrintInfo(USD, Yuan)
    
    # Call Average function for USD
    averageUSD = Average(USD)
    print("#"*46)
    print("################## Averages ##################")
    print(f"The average of the prices in USD is: ${averageUSD:.2f}")
    
    # Call Average function for Yuan
    averageYuan = Average(Yuan)
    print(f"The average of the prices in Yuan is: ¥{averageYuan:.2f}\n\n")
    
    # Call FindPrice function
    FindPrice(USD, Yuan)
main()