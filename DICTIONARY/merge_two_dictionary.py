# MERGE TWO DICTIONARY
my_dict={"a":2,"b":3,"c":4,"d":5}
dict_2={"deepanshu":18,"chetan":18}

# using update method
my_dict.update(dict_2)
print(my_dict)


# method loop
my_dict={"a":2,"b":3,"c":4,"d":5}
dict_2={"deepanshu":18,"chetan":18}
merged={}
for key in my_dict:
    merged[key]=my_dict[key]
for key in dict_2:
    merged[key]=dict_2[key]
print(merged)