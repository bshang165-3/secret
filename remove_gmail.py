import os
import pickle

if os.path.exists("all_gmail_accounts.pickle"):
    with open("all_gmail_accounts.pickle", "rb") as f:
       all_gmail_accts = pickle.load(f)

to_remove = input("What would you like to remove?")

del all_gmail_accts[to_remove]

with open("all_gmail_accounts.pickle", "wb") as f:
       pickle.dump(all_gmail_accts, f)