lst1 =[int(x) for x in input("Enter a numer: ").split()]
lst2 = [int(x) for x in input("Enter a numer: ").split()]
total = []
for i in range(min(len(lst1),len(lst2))):
    total.append(lst1[i] + lst2[i])

if len(lst1) > len(lst2):
    total.extend(lst1[len(lst2):])
else:
    total.extend(lst2[len(lst1):])  

print("Final output: ",total)