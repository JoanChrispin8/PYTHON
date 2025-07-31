num =[int(x) for x in input("Enter a number: ").split()]
b=[]
for i in num:
    if i not in b:
        b.append(i)
print("removed list : ",b)        