#!/usr/bin/env python3
"""
Simple interactive calculator.
Supports: add, subtract, multiply, divide.
Run it and follow the prompts. Enter 'q' at any prompt to quit.
"""

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ('q', 'quit', 'exit'):
            return None
        try:
            return float(s)
        except ValueError:
            print("Invalid number, try again or enter 'q' to quit.")


def calculator():
    menu = """Select operation:
1) Add (+)
2) Subtract (-)
3) Multiply (*)
4) Divide (/)
q) Quit
"""
    while True:
        print(menu)
        choice = input("Choice: ").strip().lower()
        if choice in ('q', 'quit', 'exit'):
            print("Goodbye!")
            break
        if choice not in ('1', '2', '3', '4', '+', '-', '*', '/'):
            print("Invalid choice, please try again.")
            continue

        a = get_number("Enter first number (or 'q' to quit): ")
        if a is None:
            print("Goodbye!")
            break
        b = get_number("Enter second number (or 'q' to quit): ")
        if b is None:
            print("Goodbye!")
            break

        if choice in ('1', '+'):
            res = a + b
            op = '+'
        elif choice in ('2', '-'):
            res = a - b
            op = '-'
        elif choice in ('3', '*'):
            res = a * b
            op = '*'
        else:  # divide
            op = '/'
            if b == 0:
                print("Error: Division by zero.")
                continue
            res = a / b

        print(f"{a} {op} {b} = {res}\n")


if __name__ == "__main__":
    try:
        calculator()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
