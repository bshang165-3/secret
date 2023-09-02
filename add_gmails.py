import pickle
import os
import re

if os.path.exists("all_gmail_accounts.pickle"):
    with open("all_gmail_accounts.pickle", "rb") as f:
       all_gmail_accts = pickle.load(f)
else:
    all_gmail_accts = {}

print(all_gmail_accts)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

gmail_acc = ''
while gmail_acc != 'Q':
    gmail_acc = input("What Gmail account do you want to add? Type 'Q' to quit: ")
    if gmail_acc == 'Q':
        break
    if is_valid_email(gmail_acc):
        app_pw = input("What's your app-specific password? https://myaccount.google.com/u/3/apppasswords ")
        all_gmail_accts[gmail_acc] = app_pw
    else:
        continue

for key, value in all_gmail_accts.items():
    print(key, value)

with open("all_gmail_accounts.pickle", "wb") as f:
    pickle.dump(all_gmail_accts, f)
