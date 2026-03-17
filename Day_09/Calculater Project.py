import art
from art import logo

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1,n2):
    return n1 - n2

def division(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division,
}
def calculator():
    print(art.logo)
    continue_working = True
    v1 = float(input("enter your first number: ".title()))
    while continue_working:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("chose your operators: ".title())
        v2 = float(input("enter your second number: ".title()))
        work = (operations[operation_symbol](v1,v2))
        print(f"{v1} {operation_symbol} {v2} = {work}")

        choice = input(f"Type 'y' to continue calculating with previous {work} or Type 'n' for new calculations ")

        if choice == "y":
            v1 = work
        else:
            continue_working = False
            print("\n" * 20)
            calculator()

calculator()