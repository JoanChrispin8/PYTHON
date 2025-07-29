#simple
a=input("Enter a number or string:")
if a == a[::-1]:
    print("This is Palindrome")
else:
    print("This is not Palindrome")

#while loop
n=input("Enter a value:")
i=0
j=len(n)-1
palindrome = True
while i<j:
    if n[i] != n[j]:
        palindrome = False
        break
    i += 1
    j -= 1
print("palindrome" if palindrome else "not a palindrome")    
