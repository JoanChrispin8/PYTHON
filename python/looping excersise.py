# timer with looping

count = 5

while count > 0:
    print(f"Countdown : {count}")
    count -=1
          
print("Time is Up")

# add cart

items = []

while True:
    item = input("Add item (type 'done' to finish) :")
    if item.lower() == 'done':
        break
    items.append(item)
print(items)
