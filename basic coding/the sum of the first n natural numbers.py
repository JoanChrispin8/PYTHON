#usinf forloop
a = int(input("Enter a number:"))
b=0
for i in range(a+1):
    b += i
print(b)    

# using sum() and range
print(sum(range(1,a+1)))

#using formula  a*(n+1)//2

num = int(input("Enter a number:"))
print(num*(num+1)//2)   