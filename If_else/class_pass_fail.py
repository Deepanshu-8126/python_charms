#5-- Class pass or fail
m1 = int(input("Enter first subject marks :"))

m2 = int(input("Enter second subject marks :"))

m3 = int(input("Enter third subject marks :"))

m4= int(input("Enter fourth subject marks :"))

m5 = int(input("Enter fifth subject marks :"))

total = m1+m2+m3+m4+m5

percentage = total/500 *100

if percentage>=90:
    print("Pass , Grade : A")
elif percentage<=40:
    print("Fail")
print("Total marks is :", total)
print("Percentage is :", percentage)
