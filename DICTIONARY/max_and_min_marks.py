# Minimum and maximum marks subject print
students = {
    "R": 85,
    "Python": 92,
    "C": 78,
    "Economics": 76,
}
max_marks = max(students.values())
min_marks = min(students.values())

for subject, values in students.items(): #key -- subjects : marks : value
   if values ==max_marks:
     print(f"Maximum marks {values}")
   elif values==min_marks:
    print(f"Minimum marks {values}")


# check r key exist in key or not
if "R" in students.keys():
    print("yes")