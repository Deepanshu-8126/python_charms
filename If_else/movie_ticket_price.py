#Question -- Movie ticket based on age
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 18:
    price = 100
elif age <= 60:
    price = 150
else:
    price = 80

print("Ticket Price:", price)
