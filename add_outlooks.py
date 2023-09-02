import pickle
import os
import re

if os.path.exists("all_outlook_accounts.pickle"):
    with open("all_outlook_accounts.pickle", "rb") as f:
        all_outlook_accts = pickle.load(f)
else:
    all_outlook_accts = {}

print(all_outlook_accts)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

outlook_acc = ''
while outlook_acc != 'Q':
    outlook_acc = input("What Outlook account do you want to add? Type 'Q' to quit: ")
    if outlook_acc == 'Q':
        break
    if is_valid_email(outlook_acc):
        app_pw = input("What's your app-specific password? ")
        all_outlook_accts[outlook_acc] = app_pw
    else:
        continue

for key, value in all_outlook_accts.items():
    print(key, value)

with open("all_outlook_accounts.pickle", "wb") as f:
    pickle.dump(all_outlook_accts, f)