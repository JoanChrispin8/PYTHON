def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    return a / b

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Division\n5. Exit")
    choice = input("Enter a choice: ")
    
    if choice == '5':
        break
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    if choice == '1':
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", sub(a, b))
    elif choice == "3":
        print("Result:", mul(a, b))
    elif choice == "4":
        if b != 0:
            print("Result:", div(a, b))
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation")
