nums = list(map(int, input("Enter a numbers: ").split(",")))
squared =set(map(lambda x: x**2,nums))
print(squared)  