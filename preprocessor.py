# Step1. [10 points]  
# Preprocessing:  Implement preprocessing functions for tokenization and stopword removal. 
#                 The index terms will be all the words left after filtering out markup that is not part of 
#                 the text, punctuation tokens, numbers, stopwords, etc. Optionally, you can use the Porter stemmer 
#                 to stem the index words. 
# • Input: Documents that are read one by one from the collection
# • Output: Tokens to be added to the index (vocabulary)

import os
import string


#make hash table <doc name, bag of words>
documentdictionary = {}

#make set of stop words from reading stop word file 
def getStopWords():
    file = open('testing_files/stopwords.txt','r')
    stopwords = set()
    while True: 
        line=file.readline()
        if not line:
            break
        stopwords.add(line.strip())
    return stopwords

stopwords = getStopWords()

def getDocumentName(line):
    return line[(line.index(">")+1):line.index("<",1)].strip()

def getTag(line):
    try:
        if line.index("<") == 0:
            return line[(line.index("<")+1): line.index(">",1)]
    except ValueError:
        return 'NA'
    
def tokenizeDoc(text):
    modifiedpunctuation = string.punctuation.replace("-","")
    lowercase = text.lower()
    nopunctuation = lowercase.translate(str.maketrans('', '', modifiedpunctuation))
    umodifiedtokens = nopunctuation.split(" ")
    modifiedtokens=[]

    for word in umodifiedtokens:
        if word in stopwords or word == "" or word.isnumeric(): # isnumeric will only continue if the word is an integer
            continue
        else: 
            modifiedtokens.append(word)
    
    #stemm 
            
    return modifiedtokens

def processFile(filepath):

    with open(filepath) as file:

        documentname=""
        documentrawtext = ""
        documenttokens=[]

        for line in file:
            tag = getTag(line)
            match tag:
                case "DOCNO":
                    documentname = getDocumentName(line)
                    continue
                
                case "/DOC": 
                    documenttokens=tokenizeDoc(documentrawtext)
                    documentdictionary.update({documentname: documenttokens.copy()})

                    documentname, documentrawtext = "", ""
                    documenttokens.clear()
                    continue 
                        
                case "NA":
                    documentrawtext += line.replace("\n", " ")
                    continue

                case _ :
                    continue
                                          
# a token is a word that is not a common word (like the, a, of...)
# The tokens in the phrase "The dog is red" are "dog" and "red"
def processCorpus():
    with os.scandir('coll/') as entries: 
        for entry in entries:
            processFile(entry)


