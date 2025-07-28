#using while loop
num = int(input("Enter a nember:"))
n = num
rev = 0
while num:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)    

#using slicing
n=input("Enter a number:")
print("Reversed:",int(n[::-1]))

#recursive
def reverse(a, REV=0):
    if a == 0:
        return REV  
    return reverse(a // 10, REV * 10 + a % 10)

a = int(input("Enter a number: "))
print("Reversed:", reverse(a))
