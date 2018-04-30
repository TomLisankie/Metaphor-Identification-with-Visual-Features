'''
Purpose: To lemmatize, tag, and parse the text of the entire Wikipedia
TODOs:
- Open file in a manageable way
- Lemmatize
- Tag
- Parse
'''

#import nltk

with open("data/wiki-text.txt", "r") as r, open("data/wiki-text.txt", "w") as w:
    for line in r:
        print(line)