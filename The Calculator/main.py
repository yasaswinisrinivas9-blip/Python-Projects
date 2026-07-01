import art

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# print(operations["+"](3,4))

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True
    
    while should_continue:
      for symbol in operations:
         print(symbol)
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What is the second number?: "))
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    
      choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    
      if choice == "y":
          num1 = answer
      else:
          should_continue = False
          print("\n" * 30)
          calculator()
        
    
    
calculator()