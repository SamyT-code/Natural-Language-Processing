# Step1. [10 points]  
# Preprocessing:  Implement preprocessing functions for tokenization and stopword removal. 
#                 The index terms will be all the words left after filtering out markup that is not part of 
#                 the text, punctuation tokens, numbers, stopwords, etc. Optionally, you can use the Porter stemmer 
#                 to stem the index words. 
# • Input: Documents that are read one by one from the collection
# • Output: Tokens to be added to the index (vocabulary)

import os
import string



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


def getDocumentName(line):
    return line[(line.index(">")+1):line.index("<",1)].strip()

def getTag(line):
    try:
        if line.index(">") > line.index("<"):
            return line[(line.index("<")+1): line.index(">")]
    except ValueError:
        return 'NA'
    
def tokenizeDoc(text):
    #modifiedpunctuation = string.punctuation.replace("-","")
    lowercase = text.lower().replace("-", " ")
    nopunctuation = lowercase.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    unmodifiedtokens = nopunctuation.split()
    modifiedtokens=[]


    for word in unmodifiedtokens:
        if word in stopwords or word == "" or not word.isalpha(): # isnumeric will only continue if the word is an  positive integer
            continue
        else: 
            modifiedtokens.append(word)
    
            
    return modifiedtokens

def processFile(filepath,documentdictionary,vocabset):

    with open(filepath) as file: #with automatically closes the file/directory

        documentname=""
        documentrawtext = ""
        documenttokens=[]
        textflag = False

        for line in file:
            tag = getTag(line)
            match tag:
                case "DOCNO":
                    documentname = getDocumentName(line)
                    continue
                
                case "/DOC": 
                    documenttokens=tokenizeDoc(documentrawtext)
                    documentdictionary.update({documentname: documenttokens.copy()})
                    vocabset.update(set(documenttokens.copy()))

                    documentname, documentrawtext = "", ""
                    documenttokens.clear()
                    continue 

                case "TEXT":
                    textflag = True
                    continue
                
                case "/TEXT":
                    textflag = False
                    continue 

                case "NA":
                    if(textflag == True):
                        documentrawtext += " "+ line.strip()
                    continue

                case _ :
                    continue
                                          
# a token is a word that is not a common word (like the, a, of...)
# The tokens in the phrase "The dog is red" are "dog" and "red"
def processCorpus(documentdictionary,vocabset): #documentdictionary being an empty dicitonary 
    with os.scandir('coll/') as entries: 
        
        for entry in entries:
            processFile(entry,documentdictionary,vocabset)
        
        




#main 
stopwords = getStopWords()
documentdictonary = {}
vocabset = set()

'''
processFile("testing_files/textdoc.txt",documentdictonary,vocabset)
print(vocabset)



processCorpus(documentdictonary,vocabset)
print(len(vocabset))
file = open("vocab.txt","w")
for word in vocabset:
    file.write(word+"\n")
file.close()
'''
