# Employee Salary System
# Update salary, find highest salary, salary range
from distutils.archive_util import make_zipfile

employees = {
    "E001": 50000,
    "E002": 75000,
    "E003": 45000,
    "E004": 80000,
    "E005": 60000,
    "E006": 40000
}
#  Highest salary
max_salary= max(employees.values())
print(max_salary) #80000
for emp_id,salary in employees.items():
    if salary==max_salary:
        print(f"Highest salary {emp_id},{salary}")
# update  salary
employees["E003"]=50000
print(f"UPDATED SALARY : ",employees["E003"])

# salary range
min_range=min(employees.values())
max_range=max(employees.values())
print(f"Salary range is {min_range} to {max_range}") #40000 to  80000

# average salary
total = sum(employees.values())
average=total/len(employees.keys())
print(average)

