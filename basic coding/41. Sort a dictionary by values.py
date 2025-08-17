dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = {}
items = list(dict.items())

for i in range(len(items)):
    min_dict = i
    for j in range(i+1,len(items)):
        if items[j][1] < items[min_dict][1]:
            min_dict = j
    items[i],items[min_dict] = items[min_dict],items[i]

for k,v in items:
    sorted_dict[k] = v
print("unsorted dictionary : ",dict)    
print("sorted dictionary   : ",sorted_dict)    