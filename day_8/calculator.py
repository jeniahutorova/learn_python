from art import calculator
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero")
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
print(calculator)
game_over = False
result = None
while not game_over:
    if result == None:
        n1 = float(input("Please type the first number: "))
    else:
        n1 = result
    operator = input("Please choose what operation you want to complete, type '+' to add, '-' to substract, '*' to multiply, '/' to divide: ")
    n2 = float(input("Please type a second number: "))
    if operator in operations:
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        print(f"Result is {result}")

        next_action = input(f"Type 'y' to continue calculations with {result} or type 'n' to start a new calculation: ")
        if next_action.lower() == "y":
            n1 = result
        elif next_action.lower() == "n":
            game_over = True
            print("\n" * 100)
        else:
            print("Invalid input!")
            game_over = True
    else:
        print("Invalid operator. Please try again!")
    