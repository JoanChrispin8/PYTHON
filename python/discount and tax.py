dress_amount=1200
tax = dress_amount * 0.18
total = dress_amount + tax
print(total)

if total > 1000:
    discount = total * 0.10
    total -= discount
print(total)