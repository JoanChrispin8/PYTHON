#multiplication table
number = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{i} * {number} = {i * number}")   

#while loop
i=1
while i<=10:
    print(f"\n{i} * {number} = {i*number}")    
    i += 1

#recursio
def mul_table(n,i=1):
    if i > 10:
        return
    print(f"{i} * {n} = {i*n}")
    mul_table(n,i+1)
n=int(input("Enter a number:"))
mul_table(n)    
    