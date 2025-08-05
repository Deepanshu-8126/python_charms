#Question 14 - Reverse a 3-Digit number


num = 321
hundreds = num //10
tens = (num // 10) *10
units = num %10

reversed_num = (units*100) + (tens*10 )+hundreds
print("Reversed number is :", reversed_num)