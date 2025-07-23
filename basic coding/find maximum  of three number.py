#Using max() Built-in Function
a,b,c = map(int,input("Enter three numbers with  space:").split())
print("max num is:",max(a,b,c))

#Using If-Else Conditions
 
x,y,z = map(int,input("Enter three number with sepraterd by commas:").split(","))

if x >= y and x >= z:
    maxi = x
elif y >= x  and y >= z:
    maxi =y
else:
    maxi =z
print("Max num is :",maxi)        

   