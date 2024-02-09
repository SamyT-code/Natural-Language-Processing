
'''
 index = hash table <token, list>

 Fill up the index with the tokens from preprocessor 

 Go through the tokens of individual docs -> add to  tokens list if there exist

store index as a json 

read json to get index as an object 
'''

import json
import os 
from preprocessor import getWords
from collections import Counter

def makeIndex(vocabset,documentdictionary):
    index = {}
    maxfrequency = {}

    for token in vocabset: 
        index.update({token:{}}) 

    for document in documentdictionary: #iterate through documents 
        if not documentdictionary.get(document):
            print(document)
            continue
        else:
            organizedtokens = Counter(documentdictionary.get(document))
            maxfrequency.update({document: organizedtokens.most_common(1)[0][1]})
            for token in organizedtokens: #iterate through bag of words of each doc
                if token in index: 
                    index.get(token).update({document: organizedtokens[token]})
                    #print(index.get(token))
            
    return index, maxfrequency

    
def storeHash(index, name):
    with open(name,"w") as file:
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

'''
vocabset=getWords("testing_files/vocab.txt")
documentdictionary=retrieveHash("testing_files/documentbag3.json")
stopwords = getWords("testing_files/stopwords.txt")

index, maxfrequency = makeIndex(vocabset,documentdictionary)

storeHash(index,"testing_files/invertedindex3.json")
storeHash(maxfrequency,"testing_files/maxfrequency.json")
'''