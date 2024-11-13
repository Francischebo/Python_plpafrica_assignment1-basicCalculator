# Get the user's input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Validate user input
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation entered.")
    exit()

# Perform the operation
result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 == 0:
        print("Cannot divide by zero.")
        exit()
    else:
        result = num1 / num2

# Print the result
print(f"{num1} {operation} {num2} = {result}")