print("Welcome to my calculator!")


# arithmetic operators
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: You cannot divide by zero!"

    else:
        return x / y


print("Select an operation: (1)Add (2)Subtract (3)Multiply (4)Divide")

# selects one of the 4 operators (+,-,*,/)
choice = input("Select: ")

# lists all 4 choices
if choice in ("1", "2", "3", "4"):
    first = float(input("Enter First #: "))
    second = float(input("Enter Second #: "))

    if choice == "1":
        print("Result: ", add(first, second))

    elif choice == "2":
        print("Result: ", subtract(first, second))

    elif choice == "3":
        print("Result: ", multiply(first, second))

    elif choice == "4":
        print("Result: ", divide(first, second))

else:
    print("Invalid Input")
    quit()
