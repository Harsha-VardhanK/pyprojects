#calculator
from art import logo

#Add 
def add(n1, n2):
  return n1 + n2
#Sub 
def sub(n1, n2):
  return n1 - n2 

#mul     
def mul(n1, n2):
  return n1 * n2

#div  
def div(n1, n2):
  return n1 / n2 


operations = {"+": add, "-": sub , "*": mul , "/": div}
#testing
#fun = operations["+"]
#print(fun(2, 3))

def calculator():
  print(logo)
  num1 = float(input("what is the first number : "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick a symbol of operation : ")
    num2 = float(input("what is the next number : "))
    calculator_function = operations[operation_symbol]
    answer =  calculator_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new calculation : ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
      
calculator()
  
  
