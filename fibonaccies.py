#using for loop
n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# while loop
num = int(input("\nEnter number of terms: "))
a,b =0,1
count = 0
while count < num:
    print(a, end=" ")
    a,b=b,a+b
    count +=1

# using function def fibonacci
def fibonacci_series(nu):
    a,b = 0,1
    Result = []
    for _ in range(n):
        Result.append(a)
        a,b=b,a+b
    return Result    
nu = int(input("\nEnter the number :"))
print("Fibonacci series:",fibonacci_series(nu))
    