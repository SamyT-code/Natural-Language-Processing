
'''
 index = hash table <token, list>

 Fill up the index with the tokens from preprocessor 

 Go through the tokens of individual docs -> add to  tokens list if there exist

store index as a json 

read json to get index as an object 
'''

import preprocessor

def initializeIndex(index,vocabset):
    for token in vocabset: 
        index.update({token:[]}) 

def populateIndex(index,documentdictionary):
    for key in documentdictonary.keys(): #iterate through index
        for token in documentdictionary.get(key): #iterate through bag of words of each doc
            if token in index: 
                if len(index.get(token)) == 0:
                    index.get(key).append((key,1))
                else:
                    for docs in index.get(token):
                        if token in docs: # if document already is in inverted index term list 
                            termfrequency = docs[1]
                            index.get(key).remove((key,termfrequency))
                            index.get(key).append((key,termfrequency+1))
                        else: #if document isnt already in inverted index term list 
                            index.get(key).append((key,1))

#main
stopwords = preprocessor.getStopWords()
documentdictonary = {}
vocabset = set()
index = {}

'''
processFile("testing_files/textdoc.txt",documentdictonary,vocabset)
print(vocabset)
'''


preprocessor.processFile("testing_files/textdoc.txt",documentdictonary,vocabset)
print(len(documentdictonary.get("AP880731-0079")))
print(len(vocabset))
initializeIndex(index,vocabset)
print(len(index.keys()))
print()
populateIndex(index,documentdictonary)
    
