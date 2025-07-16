# main.py
from operations import add, sub, mul, div;

def main():
  print("Welcome to the Calculator!");

  # Ask for numbers & operation
  a = float(input("Enter the first number: "));
  b = float(input("Enter the second number: "));
  op = str(input("Enter the operation (+, -, *, /): "));


  # Call functions
  if op == "+":
    result = add(a, b);
  elif op == "-":
    result = sub(a, b);
  elif op == "*":
    result = mul(a, b);
  elif op == "/":
    result = div(a, b);

  # Print result
  print(f"{a} {op} {b} = {result}");

#running program 
if __name__ == "__main__":
    main();
