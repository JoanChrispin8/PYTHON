#for loop
num = list(map(int,input("Enter a number:").split()))
total=0
for i in num:
    total += i
print("total:",total)    

#using sum
nums= list(map(int,input("Enter a number:").split()))
total=sum(nums)
print(total)

#using while loop
a=int(input("Enter a number:"))
b=0
while a>0:
    s= a % 10
    b += s
    a = a // 10
print(b)    

#using recursion
def sum_of_digits(N):
    if N == 0:
        return 0
    return(N%10) + sum_of_digits(N // 10)
N = 1234
print(sum_of_digits(N))

