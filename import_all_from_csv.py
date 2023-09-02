import csv
import pickle
# import sys
import os

def csv_to_dict(csv_filename):
    with open(csv_filename, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers if there is any
        dictionary = {}
        for rows in reader:
            if rows[12] != '':
                dictionary[rows[0]] = rows[12]
            else:
                dictionary[rows[0]] = 'Someone Affiliated With Twitch Crimes'
    return dictionary

def main():
    dir_list = os.listdir("emails/")
    csv_list = []
    for f in dir_list:
        if f.startswith("emails") and f.endswith(".csv"):
            csv_list.append(f)
    print(csv_list)

    all_dict = {}
    for csv_file in csv_list:
        temp_dict = csv_to_dict(f'emails/{csv_file}')
        all_dict.update(temp_dict)
    
    print('length of all emails is', len(all_dict))
    with open("all_employees.pickle", "wb") as f:
        pickle.dump(all_dict, f)

if __name__ == "__main__":
    main()