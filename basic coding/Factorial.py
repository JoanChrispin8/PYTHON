# for loop
n =int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} = ",fact)    

# while loop
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} = ",fact)    

#recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
num = int(input("Enter number :"))
print("Factorial of num :",factorial(num))