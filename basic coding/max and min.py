num =[int(x) for x in input("Enter a number: ").split(",")]
max_num = num[0]
min_num = num[0]
for i in num:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(f"maximum number: {max_num} and minimum number: {min_num}")
            