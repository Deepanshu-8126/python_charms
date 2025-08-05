# Question 13-- Break a 3 digit number into digit
# Example -- 456 = 4,5,6

num = 456
hundreds = num//100
tens = num//10*10
units = num % 10
print("HUNDREDS", hundreds)
print("Tens :", tens)
print("Units :", units)