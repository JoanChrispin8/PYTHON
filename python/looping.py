# for loop example
 
list = ['joan','chrispin','mugesh','santosh','nidhish']
for i in list:
    print(i.upper())

# while loop

correct_pin = '1234'
enterd_pin = ''

while enterd_pin != correct_pin:
    enterd_pin = input("enter your correct pin:")

print("access granted")

# break

for i in range(10):
    if i == 5:
        break
    print(i)

# continue
j = [1,2,-3,-4,5]

for k in j:
    if k > 0:
        continue
    print(k)

# pass

j = [1,2,-3,-4,5]

for k in j:
    pass