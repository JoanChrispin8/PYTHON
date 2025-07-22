
# Add two numbers entered by the user.

def add_int(a,b):
    return int(a) + int(b)

def add_float(a,b):
    return float(a) + float(b)

def add_complex(a,b):
    return complex(a) + complex(b)

def add_string(a,b):
    return str(a) + str(b)

a = input("Enter a value for a:")
b = input("Enter a vlaue for b:")

print("\nInteger Addition")
try:
    print(f"{a} + {b} = {add_int(a,b)}")
except:
    print("Invalid integer input")

print("/nFloat Addition")
try:
    print(f"{a} + {b} = {add_float(a,b)}")
except:
    print("Invalid float")

print("/nComplex Addition")
try:
    print(f"{a} + {b} = {add_complex(a,b)}")
except:
    print("Invalid complex")    

print("/nstring Addition")
try:
    print(f"{a} + {b} = {add_string(a,b)}")
except:
    print("Invalid string")    
 