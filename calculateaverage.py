# Task 1: Calculate the Average of Three Numbers
#Write a Python function called calculate_average that takes three numbers as input and returns their average. The function should follow these steps:

#Prompt the user to enter three numbers.
#Read the input numbers.
#Calculate the average of the three numbers.
#Return the average.

def calculate_average():
    #Prompt the user for the three numbers
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    num3 = float(input("Enter the third number:"))

    #Calculate the average
    average = (num1 + num2 + num3)/3

    #Return the average
    return average

#Call the function and print the result
result = calculate_average()
print ("The average is:", result)