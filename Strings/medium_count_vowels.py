# QUESTION-- User se ek word input lo — jaise "Education"
# Us word mein kitne vowels (a, e, i, o, u) hain — count karo aur print karo.
# Upper case ya lower case — dono ko handle karo (jaise "A" bhi vowel hai).


word = input("Enter an string ").lower()
vowel_count=0
for ch in word:
  if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    vowel_count += 1
print(vowel_count)



# Also
word = input("Enter word").lower()
vowel_count=0
for char in word:
    if char in "aeiou":
     vowel_count+=1
print(vowel_count)