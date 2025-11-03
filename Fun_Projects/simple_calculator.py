# prac_proj.py

import sys

sym = "+, -, *, /,"
X = "X"
prog_end = "\n[Program finished.]"


def divide(a, b):
    """docstring here"""
    try:
        return a / b
    except ZeroDivisionError:
        print("\nYou cannot divide by 0!")


def multiply(a, b):
    """docstring here"""
    return a * b


def add(a, b):
    """docstring here"""
    return a + b


def subtract(a, b):
    """docstring here"""
    return a - b


def main():
    """docstring here"""
    print("Simple Calcukator -->(+, -, *, /,)")
    while True:
        try:

            print(f"\nEnter any 2 numbers with any of these operators: ({sym})")
            print(f"Enter '{X}' to end program.")

            num_1 = input("\nfirst number: ").strip()
            if num_1.upper() == X:
                print(prog_end)
                sys.exit()

            operator = input(">>> ").strip()
            if operator.upper() == X:
                print(prog_end)
                sys.exit()

            if not operator:
                print("\nEnter an operator!")
                continue

            num_2 = input("second number: ").strip()
            if num_2.upper() == X:
                print(prog_end)
                sys.exit()

            mod_num1, mod_num2 = float(num_1), float(num_2)

            if operator == "/":
                result = divide(mod_num1, mod_num2)
                if result is not None:
                    print(f"\n= {result}")
                continue

            elif operator == "*":
                print("\n=", multiply(mod_num1, mod_num2))

            elif operator == "+":
                print("\n=", add(mod_num1, mod_num2))

            elif operator == "-":
                print("\n=", subtract(mod_num1, mod_num2))

        # I'm not sure we need this anymore
        except ValueError:  # Scratch that it just saved me..lol
            print("\nEnter a valid integer!")
        except KeyboardInterrupt:
            print(f"\n{prog_end}")
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

# I didn't stress too much about comments and docstrings
# This is actually a pretty simple ans straightforward program
# If you feel the need to add some..then by all means do
# I added markers for where the docstrings go
# Goodluck!
