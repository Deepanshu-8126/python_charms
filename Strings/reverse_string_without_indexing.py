# REVERSE A STRING WITHOUT INDEXING

text = input("Enter a string: ")
reversed_text = "".join(reversed(text))
print("Reversed string:", reversed_text)


# LOOP
text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print("Reversed string:", reversed_text)


text = input("Enter a string :")
rev=""
rev = text + rev
print(rev)