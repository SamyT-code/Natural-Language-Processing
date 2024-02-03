
'''
 index = hash table <token, list>

 Fill up the index with the tokens from preprocessor 

 Go through the tokens of individual docs -> add to  tokens list if there exist

store index as a json 

read json to get index as an object 
'''

import preprocessor
import json

def initializeIndex(index,vocabset):
    for token in vocabset: 
        index.update({token:{}}) 

def populateIndex(index,documentdictionary):
    count = 0
    for key in documentdictonary.keys(): #iterate through index
        for token in documentdictionary.get(key): #iterate through bag of words of each doc
            if token in index: 
                if key in index.get(token):
                    index.get(token).update({key: (index.get(token)[key]) + 1})
                else:
                    index.get(token).update({key: 1})
    


def storeHash(index):
    with open("invertedindex.json","w") as file:
        json.dump(index, file)

def retrieveHash(filename):
    try: 
        index={}
        with open(filename,"r") as file:
            index = json.load(file)
        return index
    except FileNotFoundError:
        print("Index File has not been created yet")

#main
stopwords = preprocessor.getWords("testing_files/stopwords.txt")
documentdictonary = retrieveHash("testing_files/documentbag.json")
vocab = preprocessor.getWords("testing_files/vocab.txt")
index = {}

initializeIndex(index,vocab)
print("empty index")
populateIndex(index,documentdictonary)
print("done making index")
storeHash(index)

