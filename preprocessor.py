# Step1. [10 points]  
# Preprocessing:  Implement preprocessing functions for tokenization and stopword removal. 
#                 The index terms will be all the words left after filtering out markup that is not part of 
#                 the text, punctuation tokens, numbers, stopwords, etc. Optionally, you can use the Porter stemmer 
#                 to stem the index words. 
# • Input: Documents that are read one by one from the collection
# • Output: Tokens to be added to the index (vocabulary)

#need to install numpy and nltk for this assignment 
import os
import string
from nltk.stem import PorterStemmer
import re
import json



#make set of stop words from reading stop word file 
def getWords(filename):
    file = open(filename,'r')
    words = set()
    while True: 
        line=file.readline()
        if not line:
            break
        words.add(line.strip())
    return words

def readFile(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent

def removeUnwanted(text,stopwords):
    numberless = re.sub(r'\d+', '', text)
    lowercase = numberless.lower()
    hyphensplit = lowercase.replace("'", "")
    nopunctuation = hyphensplit.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    rawtokens = nopunctuation.split()
    
    nonstemmedtokens = []
    for word in rawtokens:
        if word in stopwords or not word.isalpha():
            continue
        else:
            nonstemmedtokens.append(word)
        
    return nonstemmedtokens

def stemTokens(tokens):
    porter = PorterStemmer()
    stemmedtokens = []

    for word in tokens:
        stemmedtokens.append(porter.stem(word))
    
    return stemmedtokens

def processDoc(rawdocumenttext,stopwords):

    documentnumberpattern = re.compile(r"<DOCNO>(.*?)</DOCNO>")
    documentnumber = documentnumberpattern.findall(rawdocumenttext)

    documenttextpattern = re.compile(r"<TEXT>(.*?)</TEXT>",re.DOTALL)
    documenttext = documenttextpattern.findall(rawdocumenttext)

    headlinepattern = re.compile(r"<HEAD>(.*?)</HEAD>",re.DOTALL)
    headtext = headlinepattern.findall(rawdocumenttext)

    documenttext.extend(headtext)
    unstemmedtokens = removeUnwanted(" ".join(documenttext),stopwords)

    stemmedtokens = stemTokens(unstemmedtokens)

    tokenset = stemmedtokens.copy()

    return (documentnumber[0].strip(), stemmedtokens, tokenset)




def processFile(filetext,documentdictionary,vocabset,stopwords):
    pattern = re.compile(r'<DOC>(.*?)</DOC>',re.DOTALL)
    documentcontent = pattern.findall(filetext)

    for document in documentcontent: 
        resultstuple = processDoc(document,stopwords)
        documentdictionary.update({resultstuple[0]:resultstuple[1]})
        vocabset.update(resultstuple[2])
    

                
# a token is a word that is not a common word (like the, a, of...)
# The tokens in the phrase "The dog is red" are "dog" and "red"
def processCorpus(documentdictionary,vocabset,stopwords): #documentdictionary being an empty dicitonary 
    with os.scandir('coll/') as entries: 
        count = 0
        for entry in entries:
            filetext = readFile(entry)
            processFile(filetext,documentdictionary,vocabset,stopwords)
            count +=1 
            print(str(count) + "/322 docs completed")
    return vocabset,documentdictionary
        




#main 

'''
stopwords = getWords("testing_files/stopwords.txt")
documentdictonary = {}
vocabset = set()


processCorpus(documentdictonary,vocabset,stopwords)
print(len(vocabset))
print(len(documentdictonary))
file = open("testing_files/vocab.txt","w")
for word in vocabset:
    file.write(word+"\n")
file.close()

file2 = open("testing_files/documentbag3.json", "w")
json.dump(documentdictonary, file2)
file2.close()
'''
