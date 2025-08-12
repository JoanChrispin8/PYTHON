start = int(input("Enter a start number: "))
end = int(input("Enter an ending number: "))

for i in range(start, end + 1):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:   # Check if divisible by any number
                break
        else:
            print(i, end=' ')
