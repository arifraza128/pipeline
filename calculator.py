import os

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Cannot divide by zero"

def main():
    # Check if running in CI
    if os.getenv("CI") == "true":
        print("Running in CI mode with default inputs")
        choice = '1'
        num1 = 10
        num2 = 5
    else:
        print("Welcome to the Python Calculator!")
        print("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice")

if _name_ == "_main_":
    main()
