# -leap year check
# # leap year divisible only 400 or divibsle by 4 not 100


year=int(input("Enter a year :"))
if year%400==0:
    print("Leap year")
elif year%100==0:
    print("not a leap year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")