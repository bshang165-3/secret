import pickle

with open("all_gmail_accounts.pickle", "rb") as f:
    all_gmail_accts = pickle.load(f)

for key, value in all_gmail_accts.items():
    print(key, value)