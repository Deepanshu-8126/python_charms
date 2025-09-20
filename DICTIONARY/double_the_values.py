# DOUBLE ALL THE VALUES IN A DICTIONARY
my_dict={"a":2,"b":4,"c":6}
for key in my_dict:
    my_dict[key]=my_dict[key]*2
print(my_dict)

# another method items()
my_dict={"a":2,"b":4,"c":6}
for key,value in my_dict.items():
    my_dict[key]=value*2
print(my_dict)

