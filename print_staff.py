import pickle

with open("employees.pickle", "rb") as f:
    employees = pickle.load(f)

for employee in employees:
    print(employee, employees[employee])

print(f"length of employees.pickle is {len(employees)}")