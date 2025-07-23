#Using a Temporary Variable
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(a,b)
temp = a
a = b
b = temp
print(a,b)

#Using Tuple Unpacking
a_1 = int(input("Enter first number"))
b_1 = int(input("Enter second number"))
c = int(input("Enter third number"))
d = int(input("Enter fourth number "))
print(a_1,b_1,c,d)
a_1,b_1,c,d = d,c,b_1,a_1
print(a_1,b_1,c,d)

#Using Arithmetic Operations
a_2 = int(input("Enter first number"))
b_2 = int(input("Enter second number"))
print(a_2,b_2)
a_2 = a_2 + b_2
b_2 = a_2 - b_2
a_2 = a_2 - b_2
print(a_2,b_2)

#Using a Function 
def swap(f,g):
    return g,f
x,y =6,7
print(x,y)
x,y = swap(x,y)
print(x,y)
