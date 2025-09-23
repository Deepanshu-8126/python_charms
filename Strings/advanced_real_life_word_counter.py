# QUESTION - Take input from user and  i love python and coding check how many  times a word
# appear and count and print

sentence = input("Enter a word ")
word_list = sentence.split()

printed=[]
for char in word_list:
    if char not in printed:
      count=word_list.count(char)
      print(f"{char}: {count}")

      printed.append(char)

"""
# WITHOUT SPLIT METHOD
sentence = input("Enter a sentence: ")

# Step 1: Manually split sentence into words using loop
current_word = ""
words_list = []

for char in sentence:
    if char != ' ':          # agar space nahi hai — word banate raho
        current_word += char
    else:                    # agar space mila — word complete hua
        if current_word != "":  # blank word na daale (multiple spaces ke liye)
            words_list.append(current_word)
            current_word = ""   # next word ke liye reset


if current_word != "":
    words_list.append(current_word)

# Step 2: Count and print frequency of each word (without repetition)
printed_words = []

for word in words_list:
    if word not in printed_words:
        count = 0
        for w in words_list:
            if w == word:
                count += 1
        print(f"{word}: {count}")
        printed_words.append(word)"""