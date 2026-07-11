"""
A simple calculator module.

Provides basic arithmetic functions: add, subtract, multiply.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the result of a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def main():
    """Run a simple interactive calculator in the terminal."""
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("Choose an operation (1/2/3): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {add(a, b)}")
    elif choice == "2":
        print(f"Result: {subtract(a, b)}")
    elif choice == "3":
        print(f"Result: {multiply(a, b)}")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
