# Question 4 -- Find the greatest among 3 numbers
a = int(input("Enter the number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
if a>=b and a>=c :
    print("Greatest is : ")
elif b>=a and b>=c :
    print("B is greater")
else:
    print("C is greater")