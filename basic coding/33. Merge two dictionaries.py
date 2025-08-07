#for loop
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {}

for k in dict1:
    merged[k] = dict1[k]
for j in dict2:
    merged[j] = dict2[j]
print("1",merged)

#while loop
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
mer = {}   
key1 = list(d1.keys())
key2 = list(d2.keys())

j = 0
while j < len(key1):
    mer[key1[j]] = d1[key1[j]]
    j +=1

j = 0
while j < len(key2):
    mer[key2[j]] = d2[key2[j]]
    j +=1

print("2",mer)