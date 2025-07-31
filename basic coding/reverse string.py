#slicing
a=input("Enter a string: ")
b=a[::-1]
print(b)

#for loop
s=input("Enter a string: ")
rev=""
for ch in s:
    rev = ch + rev
print(rev)    