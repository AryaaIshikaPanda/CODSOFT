#Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero.")
        return None

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator in ("+", "-", "*", "/"):
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            if result is not None:
                print(f"Result: {result}")

        else:
            print("Error: Invalid operator.")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

calculator()