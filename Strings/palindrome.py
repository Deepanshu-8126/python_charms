# Check whether a string a palindrome or not
string = input("Enter an string :").lower()
print(string)
rev = string[::-1]
if string == rev:
    print("Palindrome number ")
else :
    print("Not a palindrome number ")