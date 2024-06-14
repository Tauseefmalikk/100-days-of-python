#calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add (n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2

operations={   #dictionary
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
  
    num1=float(input("Enter the first number"))


    for symbol in operations:
        print(symbol)
    should_continue=True    
        
        
    while should_continue:
        operation_symbol=input("pick an operation")
        num2=float(input("Enter the next number"))

        calculation_funciton=operations[operation_symbol]
        answer=calculation_funciton(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} or type 'n to start a new calculation: ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()    

#or   

# if operation_symbol == "+":
#     answer=add(num1,num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

# elif operation_symbol=="-":
#     answer=subtract(num1,num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
    
# elif operation_symbol=="*":
#     answer=multiply(num1,num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

# elif operation_symbol == "/":
#     answer=divide(num1,num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
       
