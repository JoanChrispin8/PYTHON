def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def division(a,b): return a/b if b != 0 else print("Invalid input")

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
operator = input("chouse the operations (+,-,*,/): ")

if operator == "+":
    print("output: ",add(a,b))
elif operator == "-":
    print("outputL: ",subtract(a,b))
elif operator == "*":
    print("output: ",multiply(a,b))
elif operator == "/":  
    print("Output: ",division(a,b))
else:
    print("Invalid operation")      
    