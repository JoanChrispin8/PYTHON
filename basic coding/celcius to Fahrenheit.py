#simple code
c = float(input("Enter Celsius: "))
print("Fahrenheit:", (c * 9/5) + 32)

#recursion
def c_to_f(c,f=0):
    f= (c*9//5) + 32
    return f
c = float(input("Enter a value:"))
print("Fahrenheit:",c_to_f(c))     
