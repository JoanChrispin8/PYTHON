#for loop
list_1 = [int(x) for x in input("Enter a numbers: ").split(",")]
list_2 = list(map(int, input("Enter a number: ").split(",")))
count = []
for i in list_1:
    if i in list_2 and i not in count:
        count.append(i)
print("counted common elements: ",count)        

#while loop
l_1 = [int(x) for x in input("Enter a numbers: ").split(",")]
l_2 = list(map(int, input("Enter a number: ").split(",")))
common = []
i = 0
while i < len(l_1):
    if i in l_1 and i not in common:
        common.append(i)
    i += 1
print("counted common elements: ",common)            

#recursion method
def find_common_element(ls1,ls2,j=0,com=[]):
    if j == len(ls1):
        return com
    if ls1[j] in ls2 and ls1[j] not in com:
        com.append(ls1[j])
    return find_common_element(ls1,ls2,j + 1,com) 
ls1 = [3,4,5,6,7]
ls2 = [3,5,6,7,8]
print("counted common elements:",find_common_element(ls1,ls2))