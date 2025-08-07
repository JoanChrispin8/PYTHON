#for loop 
lst = [1,2,3,4,5,6]
total = 0
for i in lst:
    total += i
print("sum of lst:",total)

#while loop
list = [int(x) for x in input("Enter a values: ").split(",")]
sum = 0
i = 0
while i < len(list):
    list[i] += sum
    i += 1
print("sum of lst:",total)  

#recursion
def sum_list(lstv):
    if not lstv:
        return 0
    return lstv[0] + sum_list(lstv[1:])
lstv = [1,2,3,4,5,6]
print("sum of lst:",sum_list(lstv))