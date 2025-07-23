#for loop
n=int(input("Enter a number:"))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not Prime")
            break 
    else:
        print("Prime")

# while loop
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    i = 2
    while i <= num // 2:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")
