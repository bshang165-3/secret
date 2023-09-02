import os
import pickle

if os.path.exists("all_outlook_accounts.pickle"):
    with open("all_outlook_accounts.pickle", "rb") as f:
        all_outlook_accts = pickle.load(f)

to_remove = input("What would you like to remove?")

del all_outlook_accts[to_remove]

with open("all_outlook_accounts.pickle", "wb") as f:
       pickle.dump(all_outlook_accts, f)