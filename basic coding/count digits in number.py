#for loop
num=input("Enter a number:")
count = 0
for i in num:
    count += 1
print("Digits:",count)    

#while loop
n = int(input("Enter a number:"))
c = 0
while n:
    c += 1
    n = n // 10
print("count:",c)    

#recursion
def count_digits(nu,co=0):
    if nu == 0:
        return 0
    return 1 + count_digits(nu // 10)
nu = int(input("Enter a number:"))
print("count digits:",count_digits(nu))