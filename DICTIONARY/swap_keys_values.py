# QUESTION -- Swap keys and values
my_dict={"a":"Deepanshu","b":"Vishal","C":"Himanshu"}
swapped={}
for key,value in my_dict.items():
    swapped[value]=key

print(swapped)