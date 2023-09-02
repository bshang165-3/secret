import os
import pickle
# import asyncio

def configure():
    config = {}
    config['name'] =  "Sadly one of Twitch's many millions of victims or one witness to many Twitch crimes"
    config['gmail'] = input("What's your Gmail Address? ")
    try:
        os.system("open https://myaccount.google.com/apppasswords")
    except:
        print("I tried launching your default browser to https://myaccount.google.com/apppasswords but failed; maybe you are not using MacOS and need to change this line.")
    config['app_pw'] = input("What's your Google Account's App Password? https://myaccount.google.com/apppasswords : Type R to re-open page: ") 
    while config['app_pw'] == "R":
        try:
            os.system("open https://myaccount.google.com/apppasswords")
        except:
            print("I tried launching your default browser to https://myaccount.google.com/apppasswords but failed; maybe you are not using MacOS and need to change this line.")
        config['app_pw'] = input("What's your Google Account's App Password? https://myaccount.google.com/apppasswords : Type R to re-open page: ")

    with open("config.pickle", "wb") as f:
        pickle.dump(config, f)

if __name__ == '__main__':
    configure()