#for loop
value = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for i in value:
    freq[i] = freq.get(i,0) + 1 
print("freuency of values in dict are: ",freq)

#while loop
value_2 = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
j=0
fr = {}
while j < len(value_2):
    v = value_2[j]
    if v in fr:
        fr[v] +=1
    else:
        fr[v] = 1
    j +=1    
print("freuency of values in dict are: ",fr)               

#reciursion
def count_freq(lst,k=0,f=None):
    if f is None:
        f = {}
    if k == len(lst):
        return f
    val = lst[k]
    f[val] = f.get(val,0) + 1
    return count_freq(lst,k+1,f)
values = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print("freuency of values in dict are: ",count_freq(values))
