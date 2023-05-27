import os

# write_to_file function is responsible for writing a given value to a specified file.
# It takes two parameters: value, which is the value to be written, and
# filename, which is the name of the file to write to.
def write_to_file(value, filename):
    # the "a" is a shortcut for append
    with open(filename, "a") as file:
        # It writes the value to the file, followed by a newline character ('\n'),
        # using the write method of the file object
        file.write(value + '\n')

# While loop used with a boolean True to correct any unexpected crashes from the user
while True:
    choice = input("Enter '1' to enter two numbers and an operator, or '2' to read equations from a file: ")
    if choice == '1':
#this try block is used when no problems occur. In this case, if the user inputs the first value,
      #then the user moves onto the next value.
        while True:
            try:
                value_one = float(input("Please enter the first value: "))
                continue
                break
#the except block is used when there is an exception to the code and the user has inputted the wrong value,
#as a result, we defensively programme the user to re-start
            except ValueError:
                print("Oops. That was not a valid number. Please start again...")

        filename = input("Enter the name of the text file: ")

        while True:
            try:
                value_two = float(input("Please enter the second value: "))
                continue
                break
            except ValueError:
                print("Oops. That was not a valid number. Please start again...")
#the user is given 4 options, add, substract, multiple and divide to choose from.
#By inputting the first two values, we can now choose a print option 
#1,2,3,4 are the variables
        print("Select an operation to perform ")
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")

        while True:
            try:
                operation = int(input("Please enter an operation to perform: "))
                if operation not in [1, 2, 3, 4]:
                    print("Invalid choice of operations. Please choose between 1 to 4")
                    continue
                break
            except ValueError:
                print("Oops. That was not a valid number. Please start again...")

#a simple if, elif, elif and else function made to give the user input options
#also using the while, true, except functions

#if 1 is chosen, then the total value of value 1 and value 2 is added. The code calculates the sum of two variables, 
# "value_one" and "value_two", and stores the result in the variable "total_value
        if operation == 1:
            total_value = value_one + value_two
            #The code uses an f-string (formatted string literal) to format a string called "output". 
#The f-string includes placeholders enclosed in curly braces {} that are replaced with the 
# corresponding values when the string is created.    
            output = f"{value_one} + {value_two} = {total_value}"
#if 2 is chosen, then the total value of value 1 and value 2 is subtracted. 
        elif operation == 2:
            total_value = value_one - value_two
            output = f"{value_one} - {value_two} = {total_value}"
#if 3 is chosen, then the total value of value 1 and value 2 is multiplied. 
        elif operation == 3:
            total_value = value_one * value_two
#if 4 is chosen, then the total value of value 1 and value 2 is divided. 

            output = f"{value_one} * {value_two} = {total_value}"
        elif operation == 4:
            try:
                total_value = value_one / value_two
                output = f"{value_one} / {value_two} = {total_value}"
#Error division by Zero code also written
#For future Atif, please remember the indentations for a function. You spent way too long figuring this out.
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid choice of operations. Please choose between 1 to 4")
            continue

        write_to_file(output, filename)
        print(output)

    elif choice == '2':
        filename = input("Enter the name of the text file: ")
        if not os.path.isfile(filename):
            print("File does not exist. Please enter a valid filename.")
            continue
        write_to_file(filename)

    else:
        print("Invalid choice. Please enter '1' or '2.'")