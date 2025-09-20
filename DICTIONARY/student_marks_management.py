# Make an student management system store names marks and find
# average highest marks ,  average marks, failed students
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 76,
    "Vikash": 29,
    "Neha": 88,
    "Rohan": 32
}
# highest scorer
max_marks=max(students.values())
for name,marks in students.items():
    if marks == max_marks:
        print(f"Highest scorer: {name} with {marks} marks")

# AVERAGE -- total students values / no of students
total = sum(students.values()) # add
print(total)

# average marks
average=total/len(students)
print(average)

# failed students
failed_students=[]
for name,marks in students.items():
    if marks<=33:
        print(f"{name} is failed with marks {marks}")
        failed_students.append(name)
print(failed_students) #vikash rohan
print(len(failed_students)) # length of failed students --2
# 2 students are failed
passed_students = 0
for marks in students.values():
    if marks >= 33:
        passed_students += 1
pass_percentage = (passed_students / len(students)) * 100
print(pass_percentage) #71 percentage

# 5. Additional info
print(f" Total Students: {len(students)}")
print(f"   Passed: {passed_students}")
print(f"   Failed: {len(failed_students)}")