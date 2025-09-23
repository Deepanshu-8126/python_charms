# QUESTION - HOW many vowels in string count
"""string = input("Enter an string")
count=0
for ch in string.lower(): # case - insensitive
    if ch in  'aeiou':
      count+=1
print("Number of vowels :",count)  #deepanshu - 4 vowels in this character

"""

# METHOD --2 string.count
string = input("Enter word ")
count = string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u')
print(count)


# LIST COMPREHENSION
string=input("ENTER WORD")
vowels = [ch for ch in string if ch in 'aeiou']
print("NUMBER OF VOWELS ARE :",vowels)
print(len(vowels))

