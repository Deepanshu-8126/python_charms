# Factorial of a number
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact  = fact*i
    return fact # none show otherwise result bhar bhej diya

print(fac(4))