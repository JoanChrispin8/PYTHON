#Basic if-else method
a =10
if a % 2 == 0:
    print("Even")
else:
    print("odd")    

#using function
def check_Odd_Even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
num = int(input())
print(check_Odd_Even(num))  

#One-Liner Expression
print( "Even" if 8 % 2 == 0 else "Odd")

#lamda function
even_odd = lambda x : "even" if x % 2 == 0 else "odd"
print(even_odd(int(input())))

#Bitwise Operator (&)
n = int(input())
if n & 1:
    print("Odd")
else:
    print("Even")    

