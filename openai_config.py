import pickle
import sys
import os

try:
    os.system("open https://platform.openai.com/account/api-keys")
except:
    pass
openai_key = input("What's your OpenAI API key? https://platform.openai.com/account/api-keys :")
with open("openai.pickle", "wb") as f:
    pickle.dump(openai_key, f)