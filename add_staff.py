import pickle
import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 add_staff.py <email> '<name>'. Make sure to include the quotes around <name>.")
        sys.exit(1)
    with open("employees.pickle", "rb") as f:
        employees = pickle.load(f)
    employees[sys.argv[1]] = sys.argv[2]
    with open("new_staff.csv", 'a') as input_file:
        csv_writer = csv.writer(input_file)
        csv_writer.writerow([sys.argv[1], sys.argv[2]])
    print(f"Added {sys.argv[2]} with email {sys.argv[1]}")
    with open("employees.pickle", "wb") as f:
        pickle.dump(employees, f)

if __name__ == "__main__":
    main()