#for loop
s=input("Enter a string: ")
vowels = "aeiouAEIOU"
count=0
for char in s:
    if char in vowels:
        count += 1
print("Count of vowels:",count)        

#while loop
h=input("Enter a string: ")
vowels = "aeiouAEIOU"
cou = 0
i = 0
while i<len(h):
    if s[i] in vowels:
        cou += 1
    i += 1
print("Count of vowels:",cou)      

#recursion
def count_string(d):
    if not d:
        return 0
    return(1 if d[0] in "aeiou" else 0) + count_string(d[1:])
d=input("Enter a string: ").lower()
print("Count of vowels:",count_string(d))