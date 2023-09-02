import pickle
import sys
import csv

input_csv_file = "emails-for-twitch-tv-1530079.csv"
output_csv_file = "former_employees.csv"

with open("employees.pickle", "rb") as f:
    employees = pickle.load(f)

for email in sys.argv[1:]:
    if email in employees:
        try:
            del employees[email]
            with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'a') as output_file:
                csv_reader = csv.reader(input_file)
                csv_writer = csv.writer(output_file)
                for row in csv_reader:
                    if row[0] == email:
                        csv_writer.writerow(row)
                print(f"Removed staff with email {email}")

        except Exception as e:
            print(e)

with open("employees.pickle", "wb") as f:
    pickle.dump(employees, f)