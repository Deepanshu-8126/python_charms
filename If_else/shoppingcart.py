# Question --online shopping cart program
# Aapne shopping ki hai.
#
# ₹500 se zyada kharch par 10% discount
#
# ₹1000 se zyada par 20% discount
#
# Nahi toh koi discount nahi

amount = float(input("Enter your total bill amount: "))

if amount > 1000:
    discount = amount * 0.2
elif amount > 500:
    discount = amount * 0.1
else:
    discount = 0

print("Discount:", discount)
print("Final amount to pay:", amount - discount)
