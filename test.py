# calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():

    operations = {"+": add, "=": subtract,
                  "*": multiply, "/": divide}
    num1 = int(input("what's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = int(input("what's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("y to continue, n to start a new one") == "y":
            num1 = answer
        else:
            calculator()


calculator()
