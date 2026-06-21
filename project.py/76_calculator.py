import calculator_art


def add (n1 , n2):
    return n1 + n2

def sub (n1 , n2):
    return n1 - n2

def mul (n1 , n2):
    return n1 * n2

def div (n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

print(calculator_art.logo)

should_continue = True
n1 = float(input("whats the first no ?"))
while should_continue :

    for symbol in operations :
        print(symbol)
    operation_symbol = input("which opertaion you want to do ? + , - , * , / ")
    n2 = float(input("whats the second no ?"))

    answer = operations[operation_symbol](n1 , n2 )

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if choice == "y":
        n1 = answer
    else:
        should_continue = False
        print("\n" * 20)