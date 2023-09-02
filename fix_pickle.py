import pickle

with open("employees.pickle", "rb") as f:
    employees_dict = pickle.load(f)

#print(employees_dict)

new_dict = {}

for key, value in employees_dict.items():
    if key.endswith('\n') or value.endswith('\n'):
        pass
    else:
        new_dict[key] = value

#print(new_dict)

with open("employees.pickle", "wb") as f:
    pickle.dump(new_dict, f)