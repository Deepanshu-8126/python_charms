# Subjects and marks average
my_dict={"Maths":56,"SST":45,"ECONOMICS":66,"English":77,"Hindi":78}
total = sum(my_dict.values())
print(total ) # 322

# except
for value in my_dict:
    total=sum(my_dict.values())
print(total)

# average marks
average=total/len(my_dict.keys())
print(average) #64.4