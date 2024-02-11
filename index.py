
import json
from collections import Counter

#given a list of words (vocabset) and tokens in each document(documentdictionary)
#function returns an inverted index of the words in vocabset
def makeIndex(vocabset,documentdictionary):
    #dictionary key is a word in the vocabulary
    #dictionary value is another dictionary that stores the document name and frequency of word in document
    index = {}

    #dicitonary stores the highest frequency of a term in a document for tf-idf normalization
    maxfrequency = {}

    #initializes index with empty values
    for token in vocabset: 
        index.update({token:{}}) 

    for document in documentdictionary: 
        #skip documents that have no text in text tag or head tag
        if not documentdictionary.get(document):
            continue

        else:
            #given all the stemmed tokens of a document(including repeats)
            #returns a dictionary containing each token and its frequency
            organizedtokens = Counter(documentdictionary.get(document))

            #gets the most frequent and adds it to maxfrequency dicitionary
            maxfrequency.update({document: organizedtokens.most_common(1)[0][1]})

            for token in organizedtokens:
                if token in index: 
                    index.get(token).update({document: organizedtokens[token]})

            
    return index, maxfrequency

# utility function that stores a dictionary as a json file in directory
def storeHash(index, name):
    with open(name,"w") as file:
        json.dump(index, file)

#utility function that reads a json in directory and returns its python object equialent
def retrieveHash(filename):
    try: 
        index={}
        with open(filename,"r") as file:
            index = json.load(file)
        return index
    except FileNotFoundError:
        print("Index File has not been created yet")

#main
