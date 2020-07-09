import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for 'Yes', or N for 'No'. " % get_close_matches(w, data.keys())[0])    
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The Word Doesn't exist"
        else:
            return "We did not get the word"

    else:
        return "The word doesn't exist in the library. Please Check again. "

word = input("Enter the word: ")
output = translate(word)

for item in output:
    print(item)


