#for loop
n = 153
power = len(str(n))
sum = 0
for i in str(n):
    sum += int(i) ** power
if n == sum:
    print("Armstrong number")
else:
    print("Not a Armstrong number")

#while loop
num = int(input("Enter a number: "))
nu = num
p =len(str(num))
s= 0
while nu > 0 :
    digits = nu % 10
    s += digits ** p 
    nu //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not a Armstrong number")    

