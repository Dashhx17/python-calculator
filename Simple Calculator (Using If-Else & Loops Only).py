print("welcome to my mini calculator")

# keep the calculator running until the user chooses to exit
# ask user to select operation
while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

# Exit the loop if user selects 5
    if choice == '5':
        print("Thank you for using my calculator. Goodbye!")
        break

# Ask user for 2 inputs and convert to float so decimals work too
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

 # Perform the operation based on user's choice
    if choice == '1':
        print("Result:", num1 + num2)

    elif choice == '2':
        print("Result:", num1 - num2)

    elif choice == '3':
        print("Result:", num1 * num2)

    elif choice == '4':
        if num2 == 0:
            print("Error: cannot divide by zero") #to avoid division by zero error
        else:
            print("Result:", num1 / num2)

    else:
        print("❌ Invalid input. Please enter a number from 1 to 5.")
